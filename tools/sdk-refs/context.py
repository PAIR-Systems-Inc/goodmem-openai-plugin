#!/usr/bin/env python3
"""Check reference navigation and context budgets with a fixed tokenizer proxy.

Reading traces are deterministic example routes, not autonomous-agent benchmarks.
Token counts include complete file contents, but exclude host/tool/chat overhead.
"""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
SKILL = HERE.parents[1] / "plugins/goodmem/skills/goodmem-sdk/SKILL.md"
LANGUAGES = ("python", "typescript", "java", "dotnet")
TASKS = ("ingest-retrieve", "register-embedder", "issue-scoped-key")
ENTRY_LIMIT, DETAIL_LIMIT, TASK_LIMIT = 1000, 2000, 6000


def local_links(path):
    result = set()
    for href in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        url = urlsplit(href)
        if not url.scheme and url.path:
            result.add((path.parent / unquote(url.path)).resolve())
    return result


def graph(skill):
    root = skill.parent.resolve()
    paths = {skill.resolve(), *(root / "references").rglob("*.md")}
    edges = {}
    for path in paths:
        edges[path] = local_links(path)
        for target in edges[path]:
            if not target.is_relative_to(root) or target not in paths:
                raise ValueError(f"Broken or out-of-bundle link: {path.relative_to(root)} -> {target}")
    reached, pending = set(), [skill.resolve()]
    while pending:
        path = pending.pop()
        if path not in reached:
            reached.add(path)
            pending.extend(edges[path])
    if reached != paths:
        raise ValueError("Unreachable pages: " + ", ".join(str(p.relative_to(root)) for p in sorted(paths - reached)))
    return edges


def task_trace(skill, language, task, edges):
    """Follow the overview's recipe and its explicitly selected operation/model links."""
    root = skill.parent.resolve()
    refs = root / "references"
    trace, available = [], {skill.resolve()}

    def read(path):
        if path in trace:
            return
        if path not in available:
            raise ValueError(f"Route requires an undiscovered page: {path}")
        trace.append(path)
        available.update(edges[path])

    read(skill.resolve())
    read(refs / f"{language}.md")
    recipe = refs / language / "examples" / f"{task}.md"
    read(recipe)
    for target in sorted(edges[recipe]):
        if target.parent.name not in {"models", "examples", "references"}:
            # Count namespace navigation too, even though recipes link directly.
            index = target.parent.with_suffix(".md")
            if index in edges:
                read(index)
        read(target)
    if any(p.is_relative_to(refs) and p.parts[len(refs.parts)].split(".")[0] != language for p in trace):
        raise ValueError("A task route loaded another language")
    return trace


def measure(skill=SKILL):
    import tiktoken
    from importlib.metadata import version
    if version("tiktoken") != "0.12.0":
        raise ValueError("Install requirements-checks.txt for reproducible measurements")
    encoding = tiktoken.get_encoding("o200k_base")
    edges = graph(skill)
    counts = {path: len(encoding.encode(path.read_text(), disallowed_special=())) for path in edges}
    root = skill.parent.resolve()
    pages = []
    for path, count in sorted(counts.items()):
        relative = path.relative_to(root)
        limit = ENTRY_LIMIT if len(relative.parts) <= 3 else DETAIL_LIMIT
        if count > limit:
            raise ValueError(f"{relative}: {count} tokens exceeds {limit}")
        pages.append({"file": str(relative), "tokens": count, "limit": limit})
    routes = []
    for language in LANGUAGES:
        for task in TASKS:
            trace = task_trace(skill, language, task, edges)
            total = sum(counts[p] for p in trace)
            if total > TASK_LIMIT:
                raise ValueError(f"{language}/{task}: {total} tokens exceeds {TASK_LIMIT}")
            routes.append({"language": language, "task": task, "tokens": total,
                           "files": [{"file": str(p.relative_to(root)), "tokens": counts[p]} for p in trace]})
    return {"tokenizer": "tiktoken==0.12.0/o200k_base", "measurement": "deterministic reading routes; excludes host/tool/chat overhead",
            "pages": pages, "routes": routes}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write full per-file reading traces as JSON")
    args = parser.parse_args()
    report = measure()
    print(f"{len(report['pages'])} pages passed navigation and size checks")
    for route in report["routes"]:
        print(f"{route['language']}/{route['task']}: {route['tokens']} tokens across {len(route['files'])} files")
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
