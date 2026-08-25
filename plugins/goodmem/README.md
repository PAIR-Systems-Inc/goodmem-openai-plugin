# GoodMem Plugin

This plugin packages GoodMem memory workflows for Codex in `plugins/goodmem`.

It currently includes these skills:

- `goodmem-help`
- `goodmem-memory-workflow`
- `goodmem-sdk`

## What It Covers

- creating access-controlled memory spaces on the user's GoodMem Cloud instance
- saving what the agent reads — notes, code, documents — as searchable memories
- semantic retrieval across spaces, with metadata filters and reranking
- answering questions from stored memories, with sources
- Python, TypeScript, Java, and .NET SDK references for building GoodMem into
  applications

## Plugin Structure

The plugin lives at:

- `plugins/goodmem/`

with this shape:

- `.codex-plugin/plugin.json`
  - required plugin manifest
  - defines plugin metadata and points Codex at the plugin contents

- `.mcp.json`
  - points Codex at GoodMem's hosted MCP service
  - remote streamable HTTP with OAuth: the user signs in with their GoodMem
    account in the browser — no API keys, no local server, no configuration

- `skills/`
  - the skill payload; each skill keeps the normal skill structure
  - `goodmem-sdk/references/` holds SDK API references generated from and
    version-stamped against the published packages

- `assets/`
  - logo and listing screenshots

- `LICENSE`
  - MIT, backing the manifest's license claim

## Notes

This plugin is service-backed through `.mcp.json`: all tools are served by
GoodMem's hosted gateway, the same service behind the GoodMem plugin for
ChatGPT, and connect to the user's own GoodMem Cloud instance after a one-time
browser sign-in.

The instance needs one embedder (the model that makes text searchable). When
it has none, the failure carries a one-time setup link that opens the user's
console on the right screen; the skills instruct the agent to relay it
verbatim.

GoodMem stores text: the agent reads what the user shares and saves what it
read. Destructive tools are labeled as such and remain subject to Codex's
approval flow.

Support: [docs.goodmem.ai](https://docs.goodmem.ai) · [support@pairsys.ai](mailto:support@pairsys.ai)
