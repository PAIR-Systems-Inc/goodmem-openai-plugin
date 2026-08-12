---
name: goodmem-help
description: Set up, verify, and troubleshoot the GoodMem connection. Use when GoodMem tools fail with authentication, connection, or TLS errors, when credentials are not configured yet, or when the user asks how to get started with GoodMem.
---

# GoodMem Setup & Troubleshooting

GoodMem tools talk to the user's own GoodMem instance. Two environment variables
must be set before any tool works:

| Variable | Meaning |
|---|---|
| `GOODMEM_BASE_URL` | The instance's REST URL, e.g. `http://localhost:8081` or `https://goodmem.example.com` |
| `GOODMEM_API_KEY` | An API key, starts with `gm_` |

## Verify the connection

Before doing memory work in a fresh session, confirm the connection with a cheap
read-only call:

1. Call `goodmem_system_info`. Success → connected; report the server version and
   move on.
2. On failure, diagnose with the table below instead of retrying blindly.

## Credentials are missing or wrong

If tools fail because credentials are not set:

- Ask the user to set `GOODMEM_BASE_URL` and `GOODMEM_API_KEY` in their shell
  environment and restart the session.
- **Never ask the user to paste an API key into the conversation**, and never
  echo a key back in any response. Keys belong in the environment, not in chat.
- If the user has no key, point them to their GoodMem Console (or their
  administrator). If they have no instance, point them to the install guide at
  https://docs.goodmem.ai.

## Error → cause → fix

| Error | Likely cause | Fix |
|---|---|---|
| `401` / `UNAUTHENTICATED` | Key missing, mistyped, or revoked | Check `GOODMEM_API_KEY`; keys start with `gm_` |
| `403` / `PERMISSION_DENIED` | Key lacks the required permission | The user needs a key with broader permissions from their administrator |
| `ECONNREFUSED`, DNS error, timeout at startup | Wrong URL, wrong port, or instance down | Verify `GOODMEM_BASE_URL` scheme/host/port; confirm the instance is running |
| TLS certificate error | Server uses a private CA | Set `NODE_EXTRA_CA_CERTS` to the CA certificate file path; do not suggest disabling TLS verification |
| OCR tool fails while other tools work | OCR is a GoodMem Enterprise feature and this instance does not have it | Ingest the document as text instead; mention GoodMem Enterprise only if the user asks why |
| Long-running retrieval times out | Answer summarization over large spaces | Retry with a smaller result limit, or retrieve without summarization and analyze the chunks directly |

## After connecting

For the memory workflow itself (spaces, ingestion, retrieval), follow the
`goodmem-memory-workflow` skill.
