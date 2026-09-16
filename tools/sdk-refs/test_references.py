"""Guard package coverage, navigation, overloads, and the PR #3 regressions."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

import context
import generate
import pages

REFS = generate.REFS
LANGUAGE = None
CACHE = Path(tempfile.gettempdir()) / "goodmem-sdk-refs"


def assert_models(test, model_pages, data, language):
    for model in data["models"]:
        with test.subTest(model=model["name"]):
            test.assertIn(model["name"], model_pages)
            section = model_pages[model["name"]]
            if model.get("import"):
                test.assertIn(model["import"], section)
            description = generate.javadoc_text(model["description"]) if language == "java" else model["description"]
            if description:
                test.assertIn(generate.public_text(description).strip(), section)
            for field in model["fields"]:
                test.assertIn(f'`{field["name"]}`', section)
                if not model.get("isEnum"):
                    test.assertIn(f'`{field["type"]}`', section)
                if field.get("wire"):
                    test.assertIn(f'JSON: `{field["wire"]}`', section)
                if field.get("description"):
                    description = generate.javadoc_text(field["description"]) if language == "java" else field["description"]
                    test.assertIn(generate.public_text(description).strip(), section)
                if field.get("required"):
                    test.assertIn(f'`{field["type"]}`, required', section)
            for key in ("definition", "valueDeclaration"):
                if model.get(key):
                    test.assertIn(model[key], section)
            for key in ("bases", "variants"):
                for name in model.get(key, []):
                    test.assertIn(f"`{name}`", section)


class PublicReferences(unittest.TestCase):
    def test_links_are_public_or_resolve_inside_the_bundle(self):
        context.graph(context.SKILL)
        allowed = {"pypi.org", "registry.npmjs.org", "www.nuget.org", "repo.maven.apache.org",
                   "docs.goodmem.ai", "learn.microsoft.com"}
        for path in sorted(REFS.rglob("*.md")):
            text = path.read_text()
            generate.public_text(text)
            self.assertEqual(sum(line.startswith("```") for line in text.splitlines()) % 2, 0, path)
            for link in re.findall(r"\]\(([^)]+)\)", text):
                with self.subTest(file=str(path.relative_to(REFS)), link=link):
                    parsed = urlparse(link)
                    if parsed.scheme:
                        self.assertEqual(parsed.scheme, "https")
                        self.assertIn(parsed.hostname, allowed)

    def test_major_request_bodies_are_self_contained(self):
        for language, fields in {
            "typescript": {"CreateApiKeyRequest": ["labels", "expiresAt", "apiKeyId", "ceiling"],
                           "SpaceCreationRequest": ["name", "spaceEmbedders"],
                           "EmbedderCreationRequest": ["displayName", "modelIdentifier"],
                           "LLMCreationRequest": ["modelIdentifier"], "RerankerCreationRequest": ["modelIdentifier"]},
            "dotnet": {"CreateApiKeyRequest": ["Labels", "ExpiresAt", "ApiKeyId", "Ceiling"],
                       "SpaceCreationRequest": ["Name", "SpaceEmbedders"],
                       "EmbedderCreationRequest": ["DisplayName", "ModelIdentifier"],
                       "LlmCreationRequest": ["ModelIdentifier"], "RerankerCreationRequest": ["ModelIdentifier"]},
            "java": {"CreateApiKeyRequest": ["labels", "expiresAt", "apiKeyId", "ceiling"],
                     "SpaceCreationRequest": ["name", "spaceEmbedders"],
                     "EmbedderCreationRequest": ["displayName", "modelIdentifier"],
                     "LLMCreationRequest": ["modelIdentifier"], "RerankerCreationRequest": ["modelIdentifier"]},
        }.items():
            for name, properties in fields.items():
                for prop in properties:
                    with self.subTest(language=language, model=name, field=prop):
                        self.assertIn(f"`{prop}`", (REFS / language / "models" / f"{name}.md").read_text())

    def test_source_repository_link_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "GitHub source link"):
            generate.public_text("[fields](https://github.com/example/private/blob/main/models)")

    def test_published_input_fields_and_every_method_signature_are_retained(self):
        if LANGUAGE is None:
            self.skipTest("Package metadata comparison runs with --language in each SDK job")
        CACHE.mkdir(parents=True, exist_ok=True)
        data = generate.package_data(LANGUAGE, CACHE)
        self.assertGreater(len(data["models"]), 30)
        model_pages = {p.stem: p.read_text() for p in (REFS / LANGUAGE / "models").glob("*.md")}
        self.assertEqual(set(model_pages), {model["name"] for model in data["models"]})
        assert_models(self, model_pages, data, LANGUAGE)
        methods = pages.operations(LANGUAGE, data, generate.javadoc_text)
        self.assertGreater(len(methods), 40)
        for (namespace, name), overloads in methods.items():
            text = (REFS / LANGUAGE / namespace / f"{name}.md").read_text()
            for signature, doc in overloads:
                self.assertIn(signature, text)
                for paragraph in doc.split("\n\n"):
                    if paragraph.strip():
                        self.assertIn(generate.public_text(paragraph).strip(), text)

    def test_overload_descriptions_are_deduplicated_without_losing_constraints(self):
        rendered = pages.operation_body("typescript", "sample", "create", [
            ("create(id: string)", "Common behavior.\n\nRequires an ID."),
            ("create(body: Request)", "Common behavior.\n\nRequires a body."),
            ("create(id: string, options: Options)", "Common behavior.\n\nRequires an ID."),
        ])
        self.assertEqual(rendered.count("Common behavior."), 1)
        self.assertEqual(rendered.count("Requires an ID."), 1)
        self.assertIn("Requires a body.", rendered)
        self.assertIn("create(id: string, options: Options)", rendered)

    def test_broken_links_and_unreachable_pages_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(context.SKILL.parent, root, dirs_exist_ok=True)
            orphan = root / "references/python/models/Orphan.md"
            orphan.write_text("# Unreachable\n")
            with self.assertRaisesRegex(ValueError, "Unreachable"):
                context.graph(root / "SKILL.md")
            orphan.unlink()
            (root / "references/python/memories/create.md").unlink()
            with self.assertRaisesRegex(ValueError, "Broken"):
                context.graph(root / "SKILL.md")

    def test_stale_split_pages_are_detected_and_safely_removed(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(generate, "REFS", Path(directory)):
            output = {"python.md": "<!-- sdk-ref fixture -->\n", "python/models/Kept.md": "<!-- sdk-ref fixture -->\n"}
            generate.synchronize(output, ["python"])
            stale = Path(directory) / "python/models/Stale.md"
            stale.write_text("<!-- sdk-ref fixture -->\n")
            with self.assertRaisesRegex(ValueError, "Regenerate"):
                generate.synchronize(output, ["python"], check=True)
            generate.synchronize(output, ["python"])
            self.assertFalse(stale.exists())
            stale.write_text("Handwritten file\n")
            with self.assertRaisesRegex(ValueError, "ungenerated"):
                generate.synchronize(output, ["python"])
            self.assertTrue(stale.exists())

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
        output = pages.render("typescript", generate.MATRIX["packages"]["typescript"], "1.0.320",
                              "https://registry.npmjs.org/", data, "See GoodmemConfig.", {},
                              generate.javadoc_text, generate.public_text)
        sections = {Path(path).stem: text for path, text in output.items() if "/models/" in path}
        assert_models(self, sections, data, "typescript")
        self.assertIn("request: Choice", output["typescript/sample/create.md"])
        self.assertIn("create(id: string)", output["typescript/sample/create.md"])
        self.assertIn("[Nested](Nested.md)", sections["Request"])
        self.assertIn("`string | null`, required", sections["Nested"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=sorted(generate.LANGUAGES))
    parser.add_argument("--cache", type=Path, default=CACHE)
    args = parser.parse_args()
    LANGUAGE, CACHE = args.language, args.cache.resolve()
    unittest.main(argv=[__file__])
