# GoodMem Plugin

Official plugin repository for [GoodMem](https://docs.goodmem.ai) — persistent
memory for AI workflows by [PAIR Systems, Inc.](https://pairsys.ai)

One plugin connects OpenAI experiences to GoodMem's hosted gateway, which serves
a curated tool surface against your own GoodMem Cloud instance. You sign in
once with your GoodMem account in the browser — no plugin API keys, no local
server, nothing to configure.

The shared skills support ambient recall, requested conversation saving,
document ingestion, spaces, semantic retrieval, processing diagnostics, and
SDK references. Host-specific guidance is limited to genuine interface
differences such as restarting OAuth.

GoodMem stores text: the assistant reads what you share — notes, code, a
document — and saves it when you ask, so it is searchable later.

## Getting started

You need a GoodMem Cloud account with at least one **instance** (yours or your
organization's — see [docs.goodmem.ai](https://docs.goodmem.ai)). The instance
needs one **embedder**, the model that makes text searchable; if it has none,
the plugin hands you a one-time setup link when you first try to save.
Memories live in **spaces** — containers created for a project or topic, made
for you the first time you save something.

Install GoodMem from the plugin directory. Use a GoodMem tool to begin sign-in,
then pick your team and instance.

**ChatGPT** — install GoodMem from the apps/connectors directory, sign in with your
GoodMem account, and pick the instance to connect.

If the connection ever reports it is no longer authorized (for example after
an API-key rotation on the instance), signing out and back in repairs it.

## Repository layout

```
.agents/plugins/marketplace.json   Marketplace manifest (install source)
plugins/goodmem/                   Canonical plugin package
  .codex-plugin/plugin.json        Canonical plugin manifest and listing metadata
  .mcp.json                        Shared hosted MCP connection (OAuth)
  skills/                          Memory, document, troubleshooting, and SDK skills
  assets/                          Shared logo and listing assets
```

## Maintaining SDK references

The supported packages and released server baseline are in
`tools/sdk-refs/versions.json`. Reference generation uses public PyPI, npm, Maven
Central, and NuGet packages. All four SDKs have small language overviews,
namespace indexes, operation pages, and linked request-model pages. No private
checkout or credentials are needed. Agents select one language and read only the
operations and model fields relevant to their task.

Use Python 3.12 with the supported `goodmem` package, Node 22, JDK 21, and .NET 8.
Install the parser and check dependencies, then regenerate all references:

```bash
pip install goodmem==0.1.34 -r tools/sdk-refs/requirements-checks.txt
npm ci --ignore-scripts --prefix tools/sdk-refs
python tools/sdk-refs/generate.py
python tools/sdk-refs/generate.py --check
python tools/sdk-refs/freshness.py
python tools/sdk-refs/test_python.py
python tools/sdk-refs/test_references.py --language python
python tools/sdk-refs/test_context.py
python tools/sdk-refs/context.py --report /tmp/sdk-context.json
```

The public maintenance tools live under `tools/sdk-refs`; `scripts/` remains
ignored for local internal tooling. Downloads and inspector build outputs stay
in a temporary cache (override with `--cache`). Downloaded npm, Maven, and NuGet
artifacts are SHA-256 pinned in the matrix. To update a package, record its public
artifact URL and checksum, regenerate, and review the changed methods and models.
Python introspection uses the exact installed package version in the matrix.
Edit overview/example templates under `tools/sdk-refs/templates`, not generated
reference pages. `--check` catches changed, missing, and obsolete pages;
regeneration removes obsolete generated pages and refuses to remove handwritten
files. Overloads share one operation page; identical descriptions are emitted once.

CI checks regeneration for all four languages, every extracted signature and
request field, local links, reachability, and public source URLs. It compiles and
executes the shipped ingestion/retrieval, embedder registration, scoped-key, and
pagination examples against local HTTP fixtures. It requires no GoodMem
credentials or live providers. This validates SDK request/response contracts;
it does not replace live server/provider integration tests.
`prepare_examples.py --output /tmp/sdk-examples` extracts the shipped examples
for the four language jobs in `sdk-examples.yml`.

CI enforces **1,000 tokens per entry/index**, **2,000 per detail/example page**,
and **6,000 per representative workflow reading path**, including the skill and
language overview. Counts use pinned `tiktoken==0.12.0` with `o200k_base` as a
consistent measurement proxy. Each workflow follows the overview's recipe and
its explicitly linked operations/models; unrelated optional types are not loaded.
The CI artifacts `sdk-context-reading-traces-python-*` record every file read and
its cost; Python 3.12 and 3.13 must reproduce identical reference pages.
These are deterministic reading paths, not an autonomous-agent evaluation or a
prediction of host billing; host prompts, tool output, and conversation add context.

The document skills require a hosted gateway that exposes content continuation
(`offset`, `next_offset`, `truncated`) and retrieval diagnostics (`warnings`,
`skipped_spaces`, `synthesis_error`). Verify those tool schemas before distributing
these skills. Merging or publishing a gateway image does not establish deployment.

## Support

- Documentation: [docs.goodmem.ai](https://docs.goodmem.ai)
- Contact: [support@pairsys.ai](mailto:support@pairsys.ai)

## License

MIT — see [LICENSE](LICENSE).
