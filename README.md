# GoodMem Plugin for ChatGPT and Codex

Official plugin repository for [GoodMem](https://docs.goodmem.ai) — persistent
memory for AI workflows by [PAIR Systems, Inc.](https://pairsys.ai)

The plugin lets ChatGPT and Codex store knowledge in access-controlled spaces on
your GoodMem instance and retrieve it with semantic search, reranking, and document
ingestion.

## Repository layout

```
.agents/plugins/marketplace.json   Marketplace manifest (install source)
plugins/goodmem/
  .codex-plugin/plugin.json        Plugin manifest and listing metadata
  .mcp.json                        Bundled MCP server configuration
  skills/                          Task-specific workflow guides
  assets/                          Logo and listing assets
```

## License

MIT — see [LICENSE](LICENSE).
