# Changelog

## [Unreleased]

### Added
- Hosted-service connection for both plugins: `.mcp.json` points at GoodMem's
  hosted MCP gateway (remote streamable HTTP with OAuth browser sign-in). No
  API keys, no local server, no configuration.
- ChatGPT plugin bundle (`plugins/goodmem-work`): skills for recalling team
  knowledge, saving conversations, and reading shared documents into memory.
- TypeScript (`@pairsystems/goodmem`) and .NET (`PairSystems.Goodmem.Client`)
  SDK references in the `goodmem-sdk` skill; all SDK references are generated
  from the published packages and version-stamped.
- Weekly CI check (`sdk-refs-freshness`) that fails when any SDK reference
  falls behind its package registry.
- Initial plugin scaffold: manifest, marketplace manifest, branding content
  gate.

### Changed
- Plugin READMEs follow the plugin-directory convention (What It Covers /
  Plugin Structure / Notes); the repository README carries the user-facing
  guide for both plugins.
- Product vocabulary throughout: instance, space, embedder, memory.
