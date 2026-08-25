---
name: goodmem-help
description: Verify and troubleshoot the GoodMem connection. Use when GoodMem tools fail with authorization or connection errors, when the user is not signed in yet, or when the user asks how to get started with GoodMem.
---

# GoodMem Setup & Troubleshooting

GoodMem tools talk to the user's GoodMem Cloud instance through GoodMem's
hosted service. There is nothing to configure: no URLs, no API keys, no local
server. The user signs in once with their GoodMem account and picks the
instance to connect; everything after that is automatic.

## Getting started

If GoodMem tools are not available or answer that the connection is not
authorized, the user needs to sign in:

- In Codex, run `codex mcp login goodmem` (or simply use a GoodMem tool — the
  sign-in opens automatically when needed).
- The browser opens GoodMem's own sign-in page: they sign in with their
  GoodMem account, pick a team if they have more than one, then pick the
  instance to connect.
- No GoodMem account yet → they can create one at
  [cloud.goodmem.ai/login](https://cloud.goodmem.ai/login?loc=cloud-hero), or
  ask their organization's administrator for access.

For this connection, never ask the user for an API key or an instance URL —
the sign-in flow is the only path, by design. (Writing their own application
with the GoodMem SDKs is different: there, keys from the console are the
normal way in — see the goodmem-sdk skill.)

## Verify the connection

Before doing memory work in a fresh session, confirm the connection with a
cheap read-only call: `goodmem_users_me`. Success proves the connection is
signed in and authorized — report who the user is connected as and move on.
On failure, diagnose with the table below instead of retrying blindly.

## Troubleshooting

| Error | Likely cause | Fix |
|---|---|---|
| "no longer authorized — the instance's API key was changed" | The instance's key was rotated or the grant revoked | Sign out and sign in again (`codex mcp logout goodmem`, then `codex mcp login goodmem`) — reconnecting repairs the connection automatically |
| Sign-in page rejects the email | The organization hasn't enabled access for that account | Ask the GoodMem administrator |
| The instance isn't in the picker | Wrong team selected, or the instance is still provisioning or paused | Pick the right team first; check the instance's status in the GoodMem Cloud console |
| Space creation fails with a setup link | The instance has no embedding model yet | Relay the message and link exactly as the error instructs; the user completes a one-minute setup in their console, then retry |
| A memory's `processing_status` is `FAILED` | The instance's embedding pipeline is broken — `processing_error` says why (for example an invalid provider key) | Report `processing_error` to the user; the fix happens in their GoodMem console |
| Long-running retrieval times out | Answer summarization over large spaces | Retry with a smaller result limit, or retrieve without summarization and analyze the chunks directly |

## After connecting

Hand off to the **goodmem-memory-workflow** skill for the actual memory work:
spaces, ingestion, processing, retrieval.
