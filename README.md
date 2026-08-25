# GoodMem Plugins for ChatGPT and Codex

Official plugin repository for [GoodMem](https://docs.goodmem.ai) — persistent
memory for AI workflows by [PAIR Systems, Inc.](https://pairsys.ai)

Two plugins, one service: both connect to GoodMem's hosted gateway, which
serves a curated tool surface against your own GoodMem Cloud instance. You
sign in once with your GoodMem account in the browser — no API keys, no local
server, nothing to configure.

- **GoodMem for Codex** (`plugins/goodmem`) — give your coding agent
  persistent memory: spaces for project knowledge, semantic retrieval with
  metadata filters and reranking, and SDK references for building GoodMem into
  your own applications.
- **GoodMem for ChatGPT** (`plugins/goodmem-work`) — your team's memory in
  ChatGPT: recall stored decisions, notes, and documents with sources, and
  save conversations worth keeping.

GoodMem stores text: the assistant reads what you share — notes, code, a
document — and saves what it read, so it is searchable later.

## Getting started

You need a GoodMem Cloud account with at least one **instance** (yours or your
organization's — see [docs.goodmem.ai](https://docs.goodmem.ai)). The instance
needs one **embedder**, the model that makes text searchable; if it has none,
the plugin hands you a one-time setup link when you first try to save.
Memories live in **spaces** — containers created for a project or topic, made
for you the first time you save something.

**Codex** — from the plugin directory: open `/plugins` in Codex and install
GoodMem. Or directly from this repository:

```bash
codex plugin marketplace add PAIR-Systems-Inc/goodmem-openai-plugin
codex plugin install goodmem
```

Sign in with `codex mcp login goodmem` (or just use a GoodMem tool — the
browser opens when needed), pick your team and instance, and you're connected.

**ChatGPT** — install GoodMem from the connectors directory, sign in with your
GoodMem account, and pick the instance to connect.

If the connection ever reports it is no longer authorized (for example after
an API-key rotation on the instance), signing out and back in repairs it.

## Repository layout

```
.agents/plugins/marketplace.json   Marketplace manifest (install source)
plugins/goodmem/                   The Codex plugin
  .codex-plugin/plugin.json        Plugin manifest and listing metadata
  .mcp.json                        Hosted MCP service connection (OAuth)
  skills/                          Task-specific workflow guides + SDK references
  assets/                          Logo and listing assets
plugins/goodmem-work/              The ChatGPT plugin
  .codex-plugin/plugin.json        Plugin manifest and listing metadata
  .mcp.json                        Hosted MCP service connection (OAuth)
  skills/                          Task-specific workflow guides
  assets/                          Logo and listing assets
```

## Support

- Documentation: [docs.goodmem.ai](https://docs.goodmem.ai)
- Contact: [support@pairsys.ai](mailto:support@pairsys.ai)

## License

MIT — see [LICENSE](LICENSE).
