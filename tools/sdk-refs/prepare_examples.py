#!/usr/bin/env python3
"""Extract every shipped example into disposable projects with pinned SDKs."""
import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REFS = ROOT / "plugins/goodmem/skills/goodmem-sdk/references"
FENCES = {"python": "python", "typescript": "ts", "java": "java", "dotnet": "csharp"}


def prepare(output):
    packages = json.loads((HERE / "versions.json").read_text())["packages"]
    manifest = {}

    def write(path, text):
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    for language, fence in FENCES.items():
        manifest[language] = {}
        dotnet_usings, dotnet_functions, dotnet_cases = set(), [], []
        for path in sorted((REFS / language / "examples").glob("*.md")):
            blocks = re.findall(rf"```{fence}\n(.*?)\n```", path.read_text(), re.S)
            if len(blocks) != 1:
                raise ValueError(f"Expected one complete example: {path}")
            code, name = blocks[0] + "\n", path.stem
            if language == "python":
                write(f"python/{name}.py", code)
                command = ["{python}", f"python/{name}.py"]
            elif language == "typescript":
                write(f"typescript/{name}.ts", code)
                command = ["node", f"typescript/{name}.js"]
            elif language == "java":
                cls = re.search(r"public class (\w+)", code)[1]
                write(f"java/src/main/java/{cls}.java", code)
                command = ["java", "-cp", "java/build/install/goodmem-plugin-sdk-example/lib/*", cls]
            else:
                # Lift namespace imports; keep every executable statement intact.
                dotnet_usings.update(re.findall(r"^using [\w.]+;\n", code, re.M))
                body = re.sub(r"^using [\w.]+;\n", "", code, flags=re.M)
                function = "".join(p.title() for p in name.split("-"))
                dotnet_functions.append(f"static async Task {function}() {{\n{body}\n}}\n")
                dotnet_cases.append(f'    case "{name}": await {function}(); break;')
                command = ["dotnet", "dotnet/bin/Release/net8.0/Example.dll", name]
            manifest[language][name] = command
        if language == "dotnet":
            write("dotnet/Program.cs", "".join(sorted(dotnet_usings)) + "\nswitch (args[0]) {\n"
                  + "\n".join(dotnet_cases) + '\n    default: throw new ArgumentException("Unknown example");\n}\n'
                  + "\n".join(dotnet_functions))
        if not manifest[language]:
            raise ValueError(f"No examples for {language}")

    # Check every documented TS method access, including nested namespaces.
    methods = []
    for path in sorted((REFS / "typescript").glob("*/*.md")):
        if path.parent.name not in {"models", "examples"}:
            methods.append(f"client.{path.parent.name}.{path.stem}")
    if len(methods) < 40:
        raise ValueError("TypeScript method catalogue is incomplete")
    write("typescript/methods.ts", 'import { Goodmem } from "@pairsystems/goodmem";\ndeclare const client: Goodmem;\n'
          + "\n".join(f"void {method};" for method in methods) + "\n")
    write("typescript/package.json", json.dumps({
        "name": "goodmem-plugin-sdk-example", "version": "1.0.0", "private": True, "type": "module",
        "dependencies": {packages["typescript"]["package"]: packages["typescript"]["version"]},
        "devDependencies": {"typescript": "5.8.3", "@types/node": "22.10.0"},
        "scripts": {"build": "tsc --strict --target ES2022 --module NodeNext --moduleResolution NodeNext *.ts"},
    }, indent=2) + "\n")
    write("dotnet/Example.csproj", f'''<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net8.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
  <ItemGroup><PackageReference Include="{packages['dotnet']['package']}" Version="{packages['dotnet']['version']}" /></ItemGroup>
</Project>
''')
    write("java/settings.gradle", "rootProject.name = 'goodmem-plugin-sdk-example'\n")
    write("java/build.gradle", f'''plugins {{ id 'application' }}
repositories {{ mavenCentral() }}
dependencies {{ implementation '{packages['java']['package']}:{packages['java']['version']}' }}
java {{ toolchain {{ languageVersion = JavaLanguageVersion.of(21) }} }}
application {{ mainClass = 'GoodmemExample' }}
''')
    write("examples.json", json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    prepare(parser.parse_args().output)
