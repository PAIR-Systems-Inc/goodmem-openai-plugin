---
name: goodmem-sdk
description: Versioned SDK references for building GoodMem into applications, in Python (goodmem), TypeScript (@pairsystems/goodmem), Java (ai.pairsys:goodmem-java), or .NET (PairSystems.Goodmem.Client). Use only when the user explicitly asks to write code that integrates GoodMem — spaces, ingestion, semantic retrieval, RAG pipelines. Default to Python unless they choose another language. Not for adding an embedder, reranker, or LLM to the user's own GoodMem instance — that is a one-time console link; follow using-goodmem-memory.
---

# GoodMem SDK

Use this skill for explicitly requested application code, scripts, or integrations.
Use Python unless the user chooses another language. Setting up a model in the
user's own instance is a console task: follow `using-goodmem-memory` and
`goodmem_console_setup`.

## Read only the relevant reference

1. Open the chosen language overview below. Use its tested example for a common
   workflow, or choose a namespace and operation from the linked indexes.
2. Read the operation page for exact signatures, behavior, and overload notes.
3. Open request-model pages for the arguments being constructed. Follow nested
   type links only for fields being used; optional fields do not require reading
   their entire model graph.

When search is available, search for the exact method or type name within the
chosen language directory. Do not concatenate reference directories or load
other languages. Small linked indexes provide the same navigation without shell
access.

- [Python](references/python.md)
- [TypeScript](references/typescript.md)
- [Java](references/java.md)
- [.NET](references/dotnet.md)

Each overview identifies the supported published SDK version. Server guidance
assumes GoodMem **1.0.320 or later**; older servers may lack APIs. Inspect an
existing application's installed version before reusing signatures, and do not
silently upgrade it. Read credentials from environment/configuration.

## Shared behavior

- **Spaces need an embedder.** Reuse or register one before creating a space.
  Current APIs use access policies; space creation has no public-read flag.
- **Ingestion is asynchronous.** After creation, poll until `COMPLETED`, stop on
  `FAILED`, and enforce a deadline before retrieval. Unindexed memories are
  invisible to search.
- **Retrieval is scoped and streamed.** Select the intended spaces and filters.
  Optional rerankers reorder passages; an LLM can generate an answer. Preserve
  usable passages when synthesis fails and report warnings or partial coverage.
- **Revocation is permanent.** API-key `status=INACTIVE` and DELETE perform the
  same revocation. Issue a replacement key; revoked keys cannot become ACTIVE.
  Revocation requires `DELETE_API_KEY`; label edits require `UPDATE_API_KEY`.
- **Protect credentials.** Provider error bodies can include secrets; do not
  log them or expose them in user-facing responses.
- **OCR requires Enterprise.** On other instances, ingest document text/PDF
  memories instead of calling the OCR namespace.
