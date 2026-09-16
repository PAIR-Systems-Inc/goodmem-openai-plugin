# Host validation of the split references

Verified on 2026-09-16 with Codex CLI 0.154.0, using a temporary local
marketplace containing an unchanged copy of `plugins/goodmem`.

- `codex plugin marketplace add <temporary-marketplace> --json` succeeded.
- `codex plugin add goodmem@goodmem-pr3-review --json` succeeded in 0.071 seconds.
- All **880 installed files** matched the source byte-for-byte. The **865 SDK
  skill/reference pages** passed link and reachability checks inside the installed
  cache, using the same `context.graph` check as CI.
- `codex plugin list` reported the plugin installed and enabled.
- Adding a temporary reference file and reinstalling copied it in 0.067 seconds.
  Removing it and reinstalling pruned it in 0.070 seconds. Both refreshes kept the
  same plugin version, `1.0.0`.
- The temporary plugin and marketplace were removed after verification.

These are local installation/reinstallation measurements, not network Git
refresh, ChatGPT workspace sync, or end-to-end skill execution measurements.
No missing files or file-count rejection occurred in this Codex test.

## Release checks still requiring access

ChatGPT workspace installation and synchronization have not been verified. A
headed browser launch with the existing profile did not establish a usable
automation session; the test processes were stopped without deleting the profile.
Use a test workspace and the PR's exact commit for the first import, inspect its
saved import report, then exercise **Sync now** after a second revision. Check
that the plugin loads all five skills and that a nested SDK reference opens.
Record elapsed time and any import errors; a successful Codex cache copy does
not establish ChatGPT behavior. See the official [workspace import and sync
guide](https://learn.chatgpt.com/docs/enterprise/plugin-management) and
[complete-plugin test procedure](https://developers.openai.com/plugins/deploy/connect-chatgpt#test-the-complete-plugin).

The deployed MCP URL from `plugins/goodmem/.mcp.json` returned HTTP 401 with an
OAuth challenge to a read-only `tools/list` request on 2026-09-16. No authenticated
session was available for this verification. Before distribution, an authenticated
smoke test must confirm content continuation (`offset`, `next_offset`, `truncated`)
and retrieval diagnostics (`warnings`, `skipped_spaces`, `synthesis_error`).
No deployment was changed by this PR, and a merged gateway PR or published image
is not evidence that these fields are deployed.
