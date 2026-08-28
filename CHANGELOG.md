# Changelog

## [Unreleased]

### Added
- Hosted-service connection for the plugin: `.mcp.json` points at GoodMem's
  hosted MCP gateway (remote streamable HTTP with OAuth browser sign-in). No
  API keys, no local server, no configuration.
- Shared workflows for recalling knowledge, saving
  conversations, and reading shared documents into memory.
- TypeScript (`@pairsystems/goodmem`) and .NET (`PairSystems.Goodmem.Client`)
  SDK references in the `goodmem-sdk` skill; all SDK references are generated
  from the published packages and version-stamped.
- Weekly CI check (`sdk-refs-freshness`) that fails when any SDK reference
  falls behind its package registry.
- Initial plugin scaffold: manifest, marketplace manifest, branding content
  gate.

### Changed
- Consolidated the former `goodmem` and `goodmem-work` bundles into the single
  canonical `plugins/goodmem` package. Memory, conversation, document, and
  cloud troubleshooting workflows are shared across supported hosts; SDK
  guidance remains development-task specific.
- Replaced the overlapping memory workflow skills with five clearly scoped
  skills: `using-goodmem-memory`, `save-conversation`,
  `work-with-documents`, `goodmem-troubleshooting`, and `goodmem-sdk`.
- Plugin READMEs follow the plugin-directory convention (What It Covers /
  Plugin Structure / Notes); the repository README carries the user-facing
  guide for both plugins.
- Product vocabulary throughout: instance, space, embedder, memory.
