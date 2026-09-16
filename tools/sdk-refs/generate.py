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




def typescript_data(cache):
    with tarfile.open(artifact("typescript", cache)) as archive:
        package = json.load(archive.extractfile("package/package.json"))
        if package["version"] != MATRIX["packages"]["typescript"]["version"]:
            raise ValueError("TypeScript package version mismatch")
        declarations = archive.extractfile("package/dist/index.d.ts").read()
    path = cache / "index.d.ts"
    path.write_bytes(declarations)
    return json.loads(run(["node", str(HERE / "inspect-typescript.mjs"), str(path)]))




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


def python_data():
    import enum
    import types
    import typing
    import goodmem
    from goodmem import Goodmem
    from pydantic import BaseModel
    if goodmem.__version__ != MATRIX['packages']['python']['version']:
        raise ValueError('Install the supported Python package before generating')
    catalogue = files('goodmem').joinpath('skills/reference.md').read_text()
    names = re.findall(r'^#### `([\w.]+)\(', catalogue, re.M)
    namespaces, pending, models = {}, {}, {}

    def type_name(t):
        origin, args = typing.get_origin(t), typing.get_args(t)
        if isinstance(t, type) and t.__module__.startswith('goodmem') and issubclass(t, (BaseModel, enum.Enum)):
            pending[t.__name__] = t
            return t.__name__
        if t is type(None):
            return 'None'
        if origin in (typing.Union, types.UnionType):
            return ' | '.join(type_name(a) for a in args)
        if origin is typing.Literal:
            return 'Literal[' + ', '.join(repr(a) for a in args) + ']'
        if origin:
            return getattr(origin, '__name__', str(origin)) + '[' + ', '.join(type_name(a) for a in args) + ']'
        return getattr(t, '__name__', str(t).replace('typing.', ''))

    with Goodmem(base_url='https://example.invalid', api_key='gm_reference_no_network') as client:
        for qualified in names:
            namespace, name = qualified.rsplit('.', 1)
            method = client
            for part in qualified.split('.'):
                method = getattr(method, part)
            for param, annotation in typing.get_type_hints(method).items():
                if param != 'return':
                    type_name(annotation)
            namespaces.setdefault(namespace, []).append({
                'name': name, 'signature': qualified + str(inspect.signature(method)),
                'description': inspect.getdoc(method) or '',
            })
    while set(pending) - set(models):
        name = sorted(set(pending) - set(models))[0]
        cls = pending[name]
        fields = []
        is_enum = issubclass(cls, enum.Enum)
        if is_enum:
            fields = [{'name': item.name, 'type': name, 'description': repr(item.value)} for item in cls]
        else:
            for field_name, field in cls.model_fields.items():
                description = field.description or ''
                # Pydantic validator reprs include process-specific function
                # addresses. Only declarative constraints belong in a reference.
                constraints = [str(m) for m in field.metadata
                               if type(m).__module__ == 'annotated_types']
                if constraints:
                    description += ' Constraints: ' + ', '.join(constraints) + '.'
                fields.append({'name': field_name, 'type': type_name(field.annotation),
                               'description': description, 'required': field.is_required(),
                               'optional': not field.is_required(), 'wire': field.alias})
        models[name] = {'name': name, 'description': cls.__dict__.get('__doc__') or '',
                        'fields': fields, 'isEnum': is_enum}
    if len(names) < 40:
        raise ValueError('Python namespace catalogue is incomplete')
    return {'namespaces': [{'name': n, 'methods': m} for n, m in namespaces.items()],
            'models': list(models.values())}


def package_data(language, cache):
    return python_data() if language == 'python' else {
        'typescript': typescript_data, 'java': java_data, 'dotnet': dotnet_data,
    }[language](cache)


def generate(cache, languages=None):
    import pages
    cache.mkdir(parents=True, exist_ok=True)
    if set(MATRIX['packages']) != LANGUAGES:
        raise ValueError('The supported matrix must contain all four languages')
    output = {}
    for language in languages or MATRIX['packages']:
        package = MATRIX['packages'][language]
        source = PUBLIC_PACKAGES[language].format(version=package['version'])
        intro = (HERE / 'templates' / f'{language}.md').read_text().replace('@VERSION@', package['version'])
        examples = {p.stem: p.read_text() for p in sorted((HERE / 'templates/examples' / language).glob('*.md'))}
        output.update(pages.render(language, package, MATRIX['server_baseline'], source,
                                   package_data(language, cache), intro, examples, javadoc_text, public_text))
    return output


def synchronize(output, languages, check=False):
    expected = {REFS / path for path in output}
    actual = set()
    for language in languages:
        index = REFS / f'{language}.md'
        if index.exists():
            actual.add(index)
        actual.update((REFS / language).rglob('*.md'))
    obsolete_paths = actual - expected
    if not check:
        for obsolete in obsolete_paths:
            if not obsolete.read_text().startswith('<!-- sdk-ref '):
                raise ValueError(f'Refusing to remove an ungenerated file: {obsolete}')
    stale = list(obsolete_paths)
    for path, content in output.items():
        target = REFS / path
        if not target.exists() or target.read_text() != content:
            stale.append(target)
        if not check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    if not check:
        for obsolete in obsolete_paths:
            obsolete.unlink()
    elif stale:
        raise ValueError('Regenerate references: ' + ', '.join(str(p.relative_to(REFS)) for p in sorted(stale)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=Path(tempfile.gettempdir()) / 'goodmem-sdk-refs')
    parser.add_argument('--language', choices=sorted(LANGUAGES), action='append')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    languages = args.language or list(MATRIX['packages'])
    output = generate(args.cache.resolve(), languages)
    synchronize(output, languages, args.check)
    for language in languages:
        group = [s for path, s in output.items() if path == language + '.md' or path.startswith(language + '/')]
        print(f'{language}: {len(group)} pages; {sum(len(s.encode()) for s in group)} bytes on disk')


if __name__ == '__main__':
    main()
