#!/usr/bin/env python3
"""Validate all four reference stamps, optionally checking current registries."""
import argparse
import json
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STAMP = re.compile(r"<!-- sdk-ref package=(\S+) registry=(\S+) version=(\S+) -->")
LANGUAGES = {"python", "typescript", "java", "dotnet"}


def validate(refs, matrix):
    if not re.fullmatch(r"[0-9a-f]{40}", matrix["source_commit"]):
        raise ValueError("Pin source_commit to a full commit SHA")
    packages = matrix["packages"]
    if set(packages) != LANGUAGES:
        raise ValueError("Supported matrix must contain all four SDKs")
    if {path.stem for path in refs.glob("*.md")} != LANGUAGES:
        raise ValueError("Exactly four SDK reference files are required")
    for language, package in packages.items():
        lines = (refs / f"{language}.md").read_text().splitlines()
        match = STAMP.fullmatch(lines[0]) if lines else None
        expected = tuple(package[key] for key in ("package", "registry", "version"))
        if not match or match.groups() != expected:
            raise ValueError(f"Missing or inconsistent reference stamp: {language}")
    return packages


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read()


def latest(registry, package):
    if registry == "pypi":
        return json.loads(fetch(f"https://pypi.org/pypi/{package}/json"))["info"]["version"]
    if registry == "npm":
        return json.loads(fetch(f"https://registry.npmjs.org/{package.replace('/', '%2F')}"))["dist-tags"]["latest"]
    if registry == "maven":
        group, artifact = package.split(":")
        data = fetch(f"https://repo.maven.apache.org/maven2/{group.replace('.', '/')}/{artifact}/maven-metadata.xml").decode()
        match = re.search(r"<release>([^<]+)</release>", data)
        if not match:
            raise ValueError(f"No release found for {package}")
        return match[1]
    if registry == "nuget":
        data = json.loads(fetch(f"https://api.nuget.org/v3-flatcontainer/{package.lower()}/index.json"))
        return [version for version in data["versions"] if "-" not in version][-1]
    raise ValueError(f"Unknown registry: {registry}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Validate stamps against the matrix without contacting registries")
    args = parser.parse_args()
    matrix = json.loads((HERE / "versions.json").read_text())
    packages = validate(ROOT / "plugins/goodmem/skills/goodmem-sdk/references", matrix)
    stale = []
    for language, package in packages.items():
        newest = package["version"] if args.offline else latest(package["registry"], package["package"])
        print(f'{language}: supports {package["version"]}; latest {newest}')
        if newest != package["version"]:
            stale.append(language)
    if stale:
        raise SystemExit("Refresh supported matrix and regenerate references: " + ", ".join(stale))


if __name__ == "__main__":
    main()
