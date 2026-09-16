#!/usr/bin/env python3
"""Extract the shipped examples into disposable projects using pinned packages."""
import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REFS = ROOT / "plugins/goodmem/skills/goodmem-sdk/references"


def prepare(output):
    packages = json.loads((HERE / "versions.json").read_text())["packages"]

    def write(path, text):
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def example(language, fence):
        match = re.search(rf"```{fence}\n(.*?)\n```", (REFS / f"{language}.md").read_text(), re.S)
        if not match:
            raise ValueError(f"Missing example: {language}")
        return match[1] + "\n"

    ts = example("typescript", "ts")
    # Compile every documented namespace/method access against the published
    # declarations as well as compiling and running the example.
    methods = re.findall(r"^### (client\.[\w.]+)$", (REFS / "typescript.md").read_text(), re.M)
    if len(methods) < 40:
        raise ValueError("TypeScript method catalogue is incomplete")
    write("typescript/example.ts", ts + "\n" + "\n".join(f"void {method};" for method in methods))
    write("typescript/package.json", json.dumps({
        "name": "goodmem-plugin-sdk-example", "version": "1.0.0", "private": True, "type": "module",
        "dependencies": {packages["typescript"]["package"]: packages["typescript"]["version"]},
        "devDependencies": {"typescript": "5.8.3", "@types/node": "22.10.0"},
        "scripts": {"build": "tsc --strict --target ES2022 --module NodeNext --moduleResolution NodeNext example.ts"},
    }, indent=2) + "\n")
    write("dotnet/Program.cs", example("dotnet", "csharp"))
    write("dotnet/Example.csproj", f'''<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net8.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
  <ItemGroup><PackageReference Include="{packages['dotnet']['package']}" Version="{packages['dotnet']['version']}" /></ItemGroup>
</Project>
''')
    write("java/src/main/java/GoodmemExample.java", example("java", "java"))
    write("java/settings.gradle", "rootProject.name = 'goodmem-plugin-sdk-example'\n")
    write("java/build.gradle", f'''plugins {{ id 'application' }}
repositories {{ mavenCentral() }}
dependencies {{ implementation '{packages['java']['package']}:{packages['java']['version']}' }}
java {{ toolchain {{ languageVersion = JavaLanguageVersion.of(21) }} }}
application {{ mainClass = 'GoodmemExample' }}
''')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    prepare(parser.parse_args().output)
