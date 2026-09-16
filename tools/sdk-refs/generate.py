#!/usr/bin/env python3
"""Generate SDK references from public, versioned package artifacts.

Requires the supported Python SDK, npm ci in this directory, JDK 21, and .NET 8.
Builds and downloaded artifacts stay in --cache, outside the repository.
"""
import argparse
import base64
import hashlib
import html
import inspect
import json
import os
import re
import subprocess
import tarfile
import tempfile
import urllib.request
import zipfile
from importlib.resources import files
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REFS = ROOT / "plugins/goodmem/skills/goodmem-sdk/references"
MATRIX = json.loads((HERE / "versions.json").read_text())
LANGUAGES = {"python", "typescript", "java", "dotnet"}
PUBLIC_PACKAGES = {
    "python": "https://pypi.org/project/goodmem/{version}/",
    "typescript": "https://registry.npmjs.org/@pairsystems/goodmem/{version}",
    "java": "https://repo.maven.apache.org/maven2/ai/pairsys/goodmem-java/{version}/goodmem-java-{version}-sources.jar",
    "dotnet": "https://www.nuget.org/packages/PairSystems.Goodmem.Client/{version}",
}


def artifact(language, cache):
    spec = MATRIX["packages"][language]["artifact"]
    path = cache / spec["sha256"]
    if not path.exists():
        with urllib.request.urlopen(spec["url"], timeout=30) as response:
            data = response.read()
        if hashlib.sha256(data).hexdigest() != spec["sha256"]:
            raise ValueError(f"{language}: downloaded artifact checksum mismatch")
        path.write_bytes(data)
    if hashlib.sha256(path.read_bytes()).hexdigest() != spec["sha256"]:
        raise ValueError(f"{language}: cached artifact checksum mismatch")
    return path


def run(command, **kwargs):
    result = subprocess.run(command, text=True, capture_output=True, **kwargs)
    if result.returncode:
        raise RuntimeError(f'{command[0]} failed:\n{result.stdout}\n{result.stderr}')
    return result.stdout


def public_text(text):
    # Package docstrings sometimes use links relative to the documentation site.
    text = text.replace("](/docs/", "](https://docs.goodmem.ai/docs/")
    # References must be usable without GitHub repository access. Package docs
    # and provider guides use public documentation/registry hosts instead.
    if re.search(r"https?://(?:www\.)?github\.com/", text, re.I):
        raise ValueError("Reference contains a GitHub source link; use public package documentation")
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"


def python_reference():
    import goodmem
    from goodmem import Goodmem
    version = MATRIX["packages"]["python"]["version"]
    if goodmem.__version__ != version:
        raise ValueError(f"Install goodmem=={version} before generating")
    catalogue = files("goodmem").joinpath("skills/reference.md").read_text()
    names = re.findall(r"^#### `([\w.]+)\(", catalogue, re.M)
    sections = ["## API reference\n\nSignatures and descriptions are inspected from the published package. Parameters are keyword-only.\n"]
    with Goodmem(base_url="https://example.invalid", api_key="gm_reference_no_network") as client:
        for name in names:
            method = client
            for part in name.split("."):
                method = getattr(method, part)
            sections.append(f"#### `{name}{inspect.signature(method)}`\n\n{inspect.getdoc(method) or ''}\n")
    if len(names) < 40:
        raise ValueError("Python namespace catalogue is incomplete")
    return "\n".join(sections)


def typescript_data(cache):
    with tarfile.open(artifact("typescript", cache)) as archive:
        package = json.load(archive.extractfile("package/package.json"))
        if package["version"] != MATRIX["packages"]["typescript"]["version"]:
            raise ValueError("TypeScript package version mismatch")
        declarations = archive.extractfile("package/dist/index.d.ts").read()
    path = cache / "index.d.ts"
    path.write_bytes(declarations)
    return json.loads(run(["node", str(HERE / "inspect-typescript.mjs"), str(path)]))


def typescript_reference(data):
    sections = ["## API reference\n\nRequest types, inherited fields, and nested types are included in [Request models](#request-models). Overloads retain the package's exact constraints.\n"]
    for namespace in data["namespaces"]:
        sections.append(f'## client.{namespace["name"]}\n')
        groups = {}
        for method in namespace["methods"]:
            groups.setdefault(method["name"], []).append(method)
        for name, overloads in groups.items():
            sections.append(f'### client.{namespace["name"]}.{name}\n')
            signatures = "\n".join("client." + namespace["name"] + "." + m["signature"] + ";" for m in overloads)
            sections.append(f"```ts\n{signatures}\n```\n")
            sections.extend(dict.fromkeys(m["description"] + "\n" for m in overloads if m["description"]))
    sections.append("## Request models\n\nTypes below come from the published declarations. `?` permits omission; `null` is allowed only where listed. Interfaces can inherit fields from the named base types below.\n")
    for model in data["models"]:
        sections.append(f'### {model["name"]}\n\n{model["description"]}\n')
        if model["definition"] is not None:
            declaration = ((model["valueDeclaration"] + "\n") if model["valueDeclaration"] else "") + model["declaration"]
            sections.append(f'```ts\n{declaration}\n```\n')
        else:
            if model["bases"]:
                sections.append("Inherits: " + ", ".join(f"`{base}`" for base in model["bases"]) + ".\n")
            for field in model["fields"]:
                required = "optional" if field["optional"] else "required"
                sections.append(f'- `{field["name"]}` (`{field["type"]}`, {required}): {field["description"]}')
            sections.append("")
    return "\n".join(sections)


def dotnet_data(cache):
    import xml.etree.ElementTree as ET
    with zipfile.ZipFile(artifact("dotnet", cache)) as archive:
        nuspec = ET.fromstring(archive.read("PairSystems.Goodmem.Client.nuspec"))
        version = nuspec.find(".//{*}version").text
        if version != MATRIX["packages"]["dotnet"]["version"]:
            raise ValueError(".NET package version mismatch")
        for suffix in ("dll", "xml"):
            (cache / f"Goodmem.Client.{suffix}").write_bytes(archive.read(f"lib/net8.0/Goodmem.Client.{suffix}"))
    output = cache / "dotnet-inspector"
    run(["dotnet", "build", str(HERE / "dotnet/Inspect.csproj"), "--nologo", "-c", "Release",
         "--artifacts-path", str(cache / "dotnet-build"), "-o", str(output)])
    env = dict(os.environ, DOTNET_ROLL_FORWARD="Major")
    return json.loads(run(["dotnet", str(output / "Inspect.dll"), str(cache / "Goodmem.Client.dll"),
                           str(cache / "Goodmem.Client.xml")], env=env))


def dotnet_reference(data):
    sections = ["## API reference\n\nSignatures come from the published assembly; descriptions come from its XML documentation. Request properties and nested types are included in [Request models](#request-models).\n"]
    for namespace in data["namespaces"]:
        sections.append(f'## client.{namespace["name"]}\n')
        for method in namespace["methods"]:
            sections.append(f'### {method["name"]}\n\n```csharp\npublic {method["signature"]}\n```\n\n{method["description"]}\n')
    sections.append("## Request models\n\nUse C# property names in object initializers. `required` means the compiler requires initialization; `?` indicates a nullable type. The server can impose additional conditional requirements described below. JSON names are shown where the package declares them.\n")
    for model in sorted(data["models"], key=lambda m: m["name"]):
        sections.append(f'### {model["name"]}\n\n`{model["fullName"]}`\n\n{model["description"]}\n')
        for field in model["fields"]:
            if model["isEnum"]:
                sections.append(f'- `{field["name"]}`: {field["description"]}')
            else:
                required = ", required" if field["required"] else ""
                wire = f' JSON: `{field["wire"]}`.' if field["wire"] else ""
                sections.append(f'- `{field["name"]}` (`{field["type"]}`{required}): {field["description"]}{wire}')
        sections.append("")
    return "\n".join(sections)


def java_data(cache):
    path = artifact("java", cache)
    rows = run(["java", str(HERE / "InspectJava.java"), str(path)]).splitlines()
    result = {"methods": [], "models": {}}
    for row in rows:
        kind, *encoded = row.split("\t")
        parts = [base64.b64decode(field).decode() for field in encoded]
        if kind == "method":
            result["methods"].append(parts)
        elif kind == "model":
            result["models"][parts[0]] = {"name": parts[0], "description": parts[1], "fields": [], "variants": []}
        elif kind == "variant":
            result["models"][parts[0]]["variants"].append(parts[1])
        elif kind == "field":
            name, field, field_type, description = parts
            result["models"][name]["fields"].append({"name": field, "type": field_type, "description": description})
        else:
            raise ValueError(f"Unexpected Java metadata row: {kind}")
    if len(result["methods"]) < 40:
        raise ValueError("Java namespace catalogue is incomplete")
    result["models"] = sorted(result["models"].values(), key=lambda m: m["name"])
    return result


def javadoc_text(doc):
    doc = re.split(r"<p><strong>Example|<p><strong>REST equivalent|(?m:^\s*@)", doc, maxsplit=1)[0]
    doc = re.sub(r"\{@(?:code|link|linkplain)\s+([^}]+)\}", lambda m: "`" + html.escape(m[1].lstrip("#").replace("#", ".")) + "`", doc)
    doc = re.sub(r"<p>|</p>|<br\s*/?>", "\n\n", doc)
    return html.unescape(re.sub(r"<[^>]+>", "", doc)).strip()


def java_reference(data):
    sections = ["## API reference\n\nDeclarations and descriptions come from the published source JAR. [Request models](#request-models) includes the record components, nested types, and enum constants needed for these calls. Prefer each request's `builder()` where available; typed IDs expose `from(String)`.\n"]
    current = None
    for namespace, key, signature, doc in data["methods"]:
        if namespace != current:
            current = namespace
            sections.append(f"## client.{namespace}\n")
        sections.append(f"### `{key}`\n\n```java\n{signature}\n```\n\n{javadoc_text(doc)}\n")
    sections.append("## Request models\n\nRecord component names are also accessor names and, for requests with builders, builder setter names. Boxed types allow null; server requirements and constraints are documented per field.\n")
    for model in data["models"]:
        sections.append(f'### {model["name"]}\n\n{javadoc_text(model["description"])}\n')
        if model["variants"]:
            sections.append("Permitted implementations: " + ", ".join(f'`{v}`' for v in model["variants"]) + ".\n")
        for field in model["fields"]:
            sections.append(f'- `{field["name"]}` (`{field["type"]}`): {javadoc_text(field["description"])}')
        sections.append("")
    return "\n".join(sections)


def generate(cache, languages=None):
    cache.mkdir(parents=True, exist_ok=True)
    if set(MATRIX["packages"]) != LANGUAGES:
        raise ValueError("The supported matrix must contain all four languages")
    output = {}
    for language in languages or MATRIX["packages"]:
        package = MATRIX["packages"][language]
        if language == "python":
            body = python_reference()
        elif language == "typescript":
            body = typescript_reference(typescript_data(cache))
        elif language == "dotnet":
            body = dotnet_reference(dotnet_data(cache))
        else:
            body = java_reference(java_data(cache))
        version = package["version"]
        source = PUBLIC_PACKAGES[language].format(version=version)
        intro = (HERE / "templates" / f"{language}.md").read_text().replace("@VERSION@", version)
        stamp = f'<!-- sdk-ref package={package["package"]} registry={package["registry"]} version={version} -->'
        header = (f'{stamp}\n<!-- Generated by tools/sdk-refs/generate.py from published packages. -->\n\n'
                  f'This guide supports [{package["package"]} {version}]({source}). '
                  f'Server guidance assumes GoodMem {MATRIX["server_baseline"]} or later; '
                  'older servers may not expose all APIs.\n\n'
                  '**API-key lifecycle:** `status=INACTIVE` and DELETE both permanently revoke a key. '
                  'Revoked keys cannot become ACTIVE; issue a replacement key. '
                  'Revocation requires `DELETE_API_KEY`; label edits require `UPDATE_API_KEY`.\n\n')
        output[language] = public_text(header + intro.rstrip() + "\n\n" + body.rstrip() + "\n")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path(tempfile.gettempdir()) / "goodmem-sdk-refs")
    parser.add_argument("--language", choices=sorted(LANGUAGES), action="append")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for language, content in generate(args.cache.resolve(), args.language).items():
        path = REFS / f"{language}.md"
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content)
        print(f"{language}: {len(content.splitlines())} lines")
    if stale:
        raise SystemExit("Regenerate references: " + ", ".join(stale))


if __name__ == "__main__":
    main()
