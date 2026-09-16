"""Render package metadata as small, linked reference pages."""
import os
import re
from collections import defaultdict
from pathlib import PurePosixPath

FENCES = {"python": "python", "typescript": "ts", "java": "java", "dotnet": "csharp"}
LABELS = {"python": "Python", "typescript": "TypeScript", "java": "Java", "dotnet": ".NET"}


def symbols(text, names):
    return sorted(set(re.findall(r"\b[A-Za-z_]\w*\b", text)) & set(names))


def operations(language, data, clean_doc):
    result = defaultdict(list)
    if language == "java":
        for namespace, key, signature, doc in data["methods"]:
            result[(namespace, key.split("(", 1)[0])].append((signature, clean_doc(doc)))
    else:
        for namespace in data["namespaces"]:
            for method in namespace["methods"]:
                result[(namespace["name"], method["name"])].append((method["signature"], method["description"]))
    return dict(result)


def operation_body(language, namespace, name, overloads):
    # An undocumented TS overload inherits the operation's documented behavior.
    fallback = next((doc for _, doc in overloads if doc), "")
    docs = [[p.strip() for p in (doc or fallback).split("\n\n") if p.strip()] for _, doc in overloads]
    common = [p for p in docs[0] if all(p in other for other in docs[1:])]
    groups = defaultdict(list)
    for (signature, _), paragraphs in zip(overloads, docs):
        groups["\n\n".join(p for p in paragraphs if p not in common)].append(signature)
    parts = [f"# {namespace}.{name}", "\n\n".join(common)]
    for notes, signatures in groups.items():
        parts.append("```" + FENCES[language] + "\n" + "\n".join(signatures) + "\n```")
        if notes:
            parts.append(notes)
    return "\n\n".join(p for p in parts if p)


def model_body(language, model, clean_doc):
    description = clean_doc(model["description"]) if language == "java" else model["description"]
    parts = [f'# {model["name"]}', description]
    if model.get("import"):
        parts.append(f'```{FENCES[language]}\n{model["import"]}\n```')
    if model.get("definition") is not None:
        value = (model.get("valueDeclaration") or "")
        parts.append(f'```{FENCES[language]}\n{value}\n{model["declaration"]}\n```')
    else:
        if model.get("fullName"):
            parts.append(f'`{model["fullName"]}`')
        if model.get("bases"):
            parts.append("Inherits: " + ", ".join(f"`{base}`" for base in model["bases"]) + ".")
        if model.get("variants"):
            parts.append("Permitted implementations: " + ", ".join(f"`{v}`" for v in model["variants"]) + ".")
        fields = []
        for field in model["fields"]:
            description = clean_doc(field["description"]) if language == "java" else field["description"]
            if model.get("isEnum"):
                fields.append(f'- `{field["name"]}`: {description}')
                continue
            flags = ", optional" if field.get("optional") else ", required" if field.get("required") or language == "typescript" else ""
            wire = f' JSON: `{field["wire"]}`.' if field.get("wire") else ""
            fields.append(f'- `{field["name"]}` (`{field["type"]}`{flags}): {description}{wire}')
        parts.append("\n".join(fields))
    return "\n\n".join(p for p in parts if p)


def render(language, package, baseline, source, data, intro, examples, clean_doc, normalize):
    pages = {}
    models = {m["name"]: m for m in data["models"]}
    methods = operations(language, data, clean_doc)
    stamp = f'<!-- sdk-ref package={package["package"]} registry={package["registry"]} version={package["version"]} -->'

    def put(path, body, related=(), navigation=()):
        links = []
        for label, target in navigation:
            href = os.path.relpath(target, str(PurePosixPath(path).parent))
            links.append(f"[{label}]({href})")
        footer = "\n\n" + " · ".join(links) if links else ""
        if related:
            footer += "\n\nRelated types — open only those used by your request:\n\n"
            for model_name in related:
                target = f"{language}/models/{model_name}.md"
                href = os.path.relpath(target, str(PurePosixPath(path).parent))
                footer += f"- [{model_name}]({href})\n"
        pages[path] = normalize(stamp + "\n\n" + body + footer)

    namespaces = sorted({ns for ns, _ in methods})
    overview = (f'# GoodMem {LABELS[language]} SDK\n\n'
                f'[Published package {package["version"]}]({source}); server guidance assumes GoodMem {baseline} or later.\n\n'
                + intro + "\n\n## Examples\n\n")
    for name in sorted(examples):
        overview += f'- [{name.replace("-", " ").capitalize()}]({language}/examples/{name}.md)\n'
    overview += "\n## Namespaces\n\nOpen one index, then the needed operation and models. Search for a symbol inside this language directory when search is available; avoid reading whole directories.\n\n"
    overview += "\n".join(f"- [{ns}]({language}/{ns}.md)" for ns in namespaces)
    # Client configuration and per-call options can be referenced by the overview.
    put(f"{language}.md", overview, symbols(intro, models), [("SDK rules", "../SKILL.md")])

    for namespace in namespaces:
        index = f"# {namespace}\n\nChoose the operation needed for the task.\n\n"
        index += "\n".join(f"- [{name}]({namespace}/{name}.md)" for ns, name in sorted(methods) if ns == namespace)
        put(f"{language}/{namespace}.md", index, navigation=[(LABELS[language], f"{language}.md")])
    for (namespace, name), overloads in methods.items():
        body = operation_body(language, namespace, name, overloads)
        related = symbols("\n".join(signature for signature, _ in overloads), models)
        put(f"{language}/{namespace}/{name}.md", body, related,
            [(namespace, f"{language}/{namespace}.md"), (LABELS[language], f"{language}.md")])
    for name, model in models.items():
        body = model_body(language, model, clean_doc)
        related = [m for m in symbols(body, models) if m != name]
        put(f"{language}/models/{name}.md", body, related, [(LABELS[language], f"{language}.md")])
    for name, body in examples.items():
        put(f"{language}/examples/{name}.md", body, navigation=[(LABELS[language], f"{language}.md")])
    return pages
