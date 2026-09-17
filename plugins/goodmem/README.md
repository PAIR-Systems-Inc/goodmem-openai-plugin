# GoodMem Plugin

This is the single GoodMem plugin package for OpenAI experiences. All hosts use
the same hosted MCP gateway, OAuth connection, and selected GoodMem Cloud
instance; the skills adapt their language only where the host interface differs.

It currently includes these skills:

- `using-goodmem-memory`
- `save-conversation`
- `work-with-documents`
- `goodmem-troubleshooting`
- `goodmem-sdk`

## What It Covers

- proactively recalling relevant project and team knowledge
- saving requested conversations as self-contained question-and-answer pairs
- uploading original documents for GoodMem to process and make searchable
- creating and organizing memory spaces on the user's GoodMem Cloud instance
- semantic retrieval across spaces, with metadata filters and reranking
- shared cloud connection and processing diagnostics
- Python, TypeScript, Java, and .NET SDK references for building GoodMem into
  applications

## Plugin Structure

The plugin lives at:

- `plugins/goodmem/`

with this shape:

- `.codex-plugin/plugin.json`
  - required plugin manifest
  - defines the canonical GoodMem identity and points hosts at plugin contents

- `.mcp.json`
  - points the host at GoodMem's hosted MCP service
  - remote streamable HTTP with OAuth: the user signs in with their GoodMem
    account in the browser — no API keys, no local server, no configuration

- `skills/`
  - the skill payload; each skill keeps the normal skill structure
  - `goodmem-sdk/references/` holds versioned SDK method references generated
    from the supported Python package and matching GoodMem source documentation

- `assets/`
  - logo and listing assets

- `LICENSE`
  - MIT, backing the manifest's license claim

## Notes

This plugin is service-backed through `.mcp.json`: all tools are served by
GoodMem's hosted gateway and connect to the user's own GoodMem Cloud instance
after a one-time browser sign-in. There is no local GoodMem connection path.

Behavior is shared across hosts. Authentication always uses the hosted OAuth
flow, while SDK guidance activates only for development questions rather than
during ordinary memory recall.

The instance needs one embedder (the model that makes text searchable). When
it has none, the failure carries a one-time setup link that opens the user's
console on the right screen; the skills instruct the agent to relay it
verbatim.

GoodMem stores text and original files. Requested attachment saves use
`goodmem_memories_upload`, one memory per file; GoodMem handles extraction and
chunking. The tool advertises the configured file-size limit. After updating the
gateway or this plugin, refresh the host's tool discovery and installed skills.
Destructive tools remain subject to the host's approval flow.

Support: [docs.goodmem.ai](https://docs.goodmem.ai) · [support@pairsys.ai](mailto:support@pairsys.ai)
