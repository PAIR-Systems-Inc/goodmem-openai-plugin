"""Check public usability and request-model coverage, including the PR #3 regressions."""
import argparse
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlparse

import generate

REFS = generate.REFS
LANGUAGE = None
CACHE = Path(tempfile.gettempdir()) / "goodmem-sdk-refs"


def model_sections(text):
    try:
        body = text.split("\n## Request models\n", 1)[1]
    except IndexError:
        raise AssertionError("Request model documentation is missing")
    parts = re.split(r"(?m)^### (\w+)\s*$", body)
    return dict(zip(parts[1::2], parts[2::2]))


def assert_models(test, text, data):
    sections = model_sections(text)
    for model in data["models"]:
        with test.subTest(model=model["name"]):
            test.assertIn(model["name"], sections)
            section = sections[model["name"]]
            for field in model["fields"]:
                test.assertIn(f'`{field["name"]}`', section)
                if not model.get("isEnum"):
                    test.assertIn(f'`{field["type"]}`', section)
                if field.get("wire"):
                    test.assertIn(f'JSON: `{field["wire"]}`', section)
                if field.get("description"):
                    description = generate.javadoc_text(field["description"]) if LANGUAGE == "java" else field["description"]
                    test.assertIn(description, section)
            if model.get("definition"):
                test.assertIn(model["definition"], section)
            if model.get("valueDeclaration"):
                test.assertIn(model["valueDeclaration"], section)
            for base in model.get("bases", []):
                test.assertIn(f"`{base}`", section)


class PublicReferences(unittest.TestCase):
    def test_links_are_public_or_resolve_inside_the_bundle(self):
        allowed = {"pypi.org", "registry.npmjs.org", "www.nuget.org", "repo.maven.apache.org",
                   "docs.goodmem.ai", "learn.microsoft.com"}
        for path in sorted(REFS.glob("*.md")):
            text = path.read_text()
            generate.public_text(text)
            for link in re.findall(r"\]\(([^)]+)\)", text):
                with self.subTest(file=path.name, link=link):
                    parsed = urlparse(link)
                    if parsed.scheme:
                        self.assertEqual(parsed.scheme, "https")
                        self.assertIn(parsed.hostname, allowed)
                    elif parsed.path:
                        self.assertTrue((path.parent / parsed.path).is_file())
                    else:
                        self.assertEqual(parsed.fragment, "request-models")

    def test_major_request_bodies_are_self_contained(self):
        for language, fields in {
            "typescript": {"CreateApiKeyRequest": ["labels", "expiresAt", "apiKeyId", "ceiling"],
                           "SpaceCreationRequest": ["name", "spaceEmbedders"],
                           "EmbedderCreationRequest": ["displayName", "modelIdentifier"],
                           "LLMCreationRequest": ["modelIdentifier"],
                           "RerankerCreationRequest": ["modelIdentifier"]},
            "dotnet": {"CreateApiKeyRequest": ["Labels", "ExpiresAt", "ApiKeyId", "Ceiling"],
                       "SpaceCreationRequest": ["Name", "SpaceEmbedders"],
                       "EmbedderCreationRequest": ["DisplayName", "ModelIdentifier"],
                       "LlmCreationRequest": ["ModelIdentifier"],
                       "RerankerCreationRequest": ["ModelIdentifier"]},
            "java": {"CreateApiKeyRequest": ["labels", "expiresAt", "apiKeyId", "ceiling"],
                     "SpaceCreationRequest": ["name", "spaceEmbedders"],
                     "EmbedderCreationRequest": ["displayName", "modelIdentifier"],
                     "LLMCreationRequest": ["modelIdentifier"],
                     "RerankerCreationRequest": ["modelIdentifier"]},
        }.items():
            sections = model_sections((REFS / f"{language}.md").read_text())
            for name, properties in fields.items():
                for prop in properties:
                    with self.subTest(language=language, model=name, field=prop):
                        self.assertIn(f"`{prop}`", sections[name])

    def test_source_repository_link_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "GitHub source link"):
            generate.public_text("[request fields](https://github.com/example/private/blob/main/models)")

    def test_published_input_models_and_properties_are_retained(self):
        if LANGUAGE is None:
            self.skipTest("Package metadata comparison runs in each compiled-language CI job")
        CACHE.mkdir(parents=True, exist_ok=True)
        inspect_package = {"typescript": generate.typescript_data, "dotnet": generate.dotnet_data, "java": generate.java_data}
        data = inspect_package[LANGUAGE](CACHE)
        self.assertGreater(len(data["models"]), 30)
        assert_models(self, (REFS / f"{LANGUAGE}.md").read_text(), data)

    def test_typescript_aliases_enums_inheritance_and_overloads(self):
        if LANGUAGE != "typescript":
            self.skipTest("TypeScript parser is installed in the TypeScript CI job")
        declarations = '''
export interface GoodmemConfig { baseUrl: string; }
export interface RequestOptions { timeoutMs?: number; }
export declare const Mode: { readonly ACTIVE: "ACTIVE"; readonly INACTIVE: "INACTIVE"; };
export type Mode = (typeof Mode)[keyof typeof Mode];
export interface Nested {
  /** Kept field description. */
  value: string | null;
}
export interface Base {
  /** Labels carried to the request. */
  labels?: Record<string, string>;
}
export interface Request extends Base { nested: Nested; mode?: Mode; }
export type Choice = Request | { id: string };
export declare class SampleAPI {
  create(request: Choice, options?: RequestOptions): Promise<void>;
  create(id: string): Promise<void>;
}
export declare class Goodmem { readonly sample: SampleAPI; }
'''
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "fixture.d.ts"
            source.write_text(declarations)
            result = subprocess.run(["node", str(generate.HERE / "inspect-typescript.mjs"), str(source)],
                                    check=True, capture_output=True, text=True)
        data = json.loads(result.stdout)
        self.assertEqual(len(data["namespaces"][0]["methods"]), 2)
        models = {m["name"]: m for m in data["models"]}
        self.assertEqual(models["Request"]["bases"], ["Base"])
        self.assertEqual(models["Nested"]["fields"][0]["description"], "Kept field description.")
        self.assertTrue(models["Base"]["fields"][0]["optional"])
        self.assertIn('readonly INACTIVE: "INACTIVE"', models["Mode"]["valueDeclaration"])
        text = generate.typescript_reference(data)
        assert_models(self, text, data)
        self.assertIn("request: Choice", text)
        self.assertIn("create(id: string)", text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=["typescript", "dotnet", "java"])
    parser.add_argument("--cache", type=Path, default=CACHE)
    args = parser.parse_args()
    LANGUAGE, CACHE = args.language, args.cache.resolve()
    unittest.main(argv=[__file__])
