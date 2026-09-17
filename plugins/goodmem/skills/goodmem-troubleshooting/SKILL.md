---
name: goodmem-troubleshooting
description: Verify and troubleshoot the hosted GoodMem Cloud connection, authorization, model setup, processing failures, and retrieval problems. Use when GoodMem is unavailable or the user asks how to connect or repair it.
---

# Troubleshoot GoodMem Cloud

GoodMem connects only through its hosted OAuth gateway to the user's selected
GoodMem Cloud instance. Never request an API key, instance URL, or local server
configuration for this plugin.

## Verify the connection

Call `goodmem_users_me` first. Success confirms the selected account and instance;
report the connected identity and continue with the original task.

## Diagnose failures

| Symptom | Likely cause | Action |
|---|---|---|
| Connection is unauthorized after previously working | The instance key or grant changed | Reconnect GoodMem through the current host |
| Sign-in rejects the account | Organization access is not enabled | Ask the GoodMem administrator |
| Instance is absent from the picker | Wrong team, provisioning, or paused instance | Select the correct team and check the GoodMem Cloud console |
| Space creation returns a setup link | No embedder is configured | Relay the one-time link exactly, then retry after setup |
| Memory status is `FAILED` | Embedding pipeline or provider configuration failed | Read `processing_error` and direct the user to repair it in the cloud console |
| Agent transcribes a PDF into separate text memories | Outdated instructions or an unavailable upload tool | Check that `goodmem_memories_upload` is available and refresh the plugin instructions and tool list; do not repeat the text saves |
| Upload tool or native file object is unavailable | Outdated tool discovery or the host did not provide a usable attachment | Refresh available tools or request a fresh attachment; explain the limitation without silently transcribing |
| Retrieval with synthesis times out | Large search or answer-generation workload | Reduce the result scope or retrieve without synthesis |

Do not retry authorization failures blindly.

## Reconnect through the current host

Disconnect and reconnect the GoodMem app through the current host's connection
settings. This restarts OAuth against the same hosted gateway and cloud instance.

When the user asks to create or add an embedder, reranker, or LLM, follow the
model-setup steps in `using-goodmem-memory`: call `goodmem_console_setup` with
the matching `kind` and relay the one-time console link verbatim — never write
code or collect provider keys in chat for this.
