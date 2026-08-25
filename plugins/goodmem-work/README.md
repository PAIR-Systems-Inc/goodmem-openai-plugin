# GoodMem Plugin for ChatGPT

This plugin packages GoodMem memory workflows for ChatGPT in
`plugins/goodmem-work`.

It currently includes these skills:

- `using-your-memory`
- `save-conversation`
- `work-with-documents`

## What It Covers

- recalling a team's stored decisions, notes, and documents mid-conversation,
  with sources
- saving conversations and decisions worth keeping into memory spaces
- reading shared documents and saving their contents so they are searchable
  later

## Plugin Structure

The plugin lives at:

- `plugins/goodmem-work/`

with this shape:

- `.codex-plugin/plugin.json`
  - required plugin manifest
  - defines plugin metadata and listing content

- `.mcp.json`
  - points ChatGPT at GoodMem's hosted MCP service
  - remote streamable HTTP with OAuth: the user signs in with their GoodMem
    account in the browser — no API keys, no configuration

- `skills/`
  - the skill payload; each skill keeps the normal skill structure

- `assets/`
  - logo and listing assets

## Notes

This plugin is service-backed through `.mcp.json`: the same hosted GoodMem
gateway serves this plugin and the Codex plugin, exposing one curated tool
surface against the user's own GoodMem Cloud instance.

GoodMem stores text: the assistant reads what the user shares and saves what
it read. There is deliberately no OCR tool — the model transcribes documents
itself. Destructive tools are labeled as such and remain subject to the
approval flow.

Support: [docs.goodmem.ai](https://docs.goodmem.ai) · [support@pairsys.ai](mailto:support@pairsys.ai)
