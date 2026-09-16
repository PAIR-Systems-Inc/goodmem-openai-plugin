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

The supported SDK/server matrix is in `scripts/sdk-refs/versions.json`. To
refresh references, update that matrix to a tested GoodMem revision and package
versions, install its Python SDK, then run:

```bash
python scripts/sdk-refs/generate.py --source /path/to/goodmem
python scripts/sdk-refs/generate.py --source /path/to/goodmem --check
python scripts/sdk-refs/freshness.py
python scripts/sdk-refs/test_python.py
```

Generation reads committed files at the pinned revision, so local GoodMem work
is ignored. Python signatures are inspected from the published package;
other languages use the matching maintained SDK documentation. The source
checkout needs access to the GoodMem repository. CI uses published packages and
local HTTP fixtures; it requires no GoodMem credentials or live providers.
`prepare_examples.py --output /tmp/sdk-examples` extracts the shipped examples
for the TypeScript, Java, and .NET build/run checks in `sdk-examples.yml`.

The document continuation and retrieval diagnostics require the companion
gateway changes in `goodmem-cloud-provisioning/services/work-gateway` (and the
Go replacement). Deploy that gateway update before distributing these skills.

## Support

- Documentation: [docs.goodmem.ai](https://docs.goodmem.ai)
- Contact: [support@pairsys.ai](mailto:support@pairsys.ai)

## License

MIT — see [LICENSE](LICENSE).
