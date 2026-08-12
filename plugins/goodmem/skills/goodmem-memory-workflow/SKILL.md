---
name: goodmem-memory-workflow
description: The end-to-end GoodMem memory workflow — create spaces, ingest text and documents, wait for processing, and retrieve with semantic search, metadata filters, and optional answer summarization. Use when the user wants to store knowledge, ingest files, search memories, or set up retrieval infrastructure.
---

# GoodMem Memory Workflow

GoodMem tools are named `goodmem_<namespace>_<action>` (for example
`goodmem_spaces_create`, `goodmem_memories_retrieve`). **Do not guess parameter
shapes** — discover the exact schemas through the tool definitions in this
session; they are always current. This skill covers the workflow: what to call,
in what order, and how to recover from errors.

## 1. Know the current state

Start by looking, not creating:

- `goodmem_system_info` — connection check (see the `goodmem-help` skill if it fails).
- `goodmem_spaces_list` — what spaces exist and which embedder each uses.
- `goodmem_embedders_list` — what embedding models are available.

Reuse existing spaces and embedders whenever they fit. Create new ones only
when nothing suitable exists or the user asks.

## 2. First-time provisioning (only if no embedder exists)

A space needs an embedder. If `goodmem_embedders_list` is empty:

1. `goodmem_lookup_model` with the model name the user wants (or a sensible
   default) — it fills in provider, endpoint, and dimensions automatically.
2. `goodmem_embedders_create` with the looked-up configuration. Hosted model
   providers require an API key: have the user supply it via environment or
   their Console — never request or echo secrets in the conversation.
3. Optionally register a reranker (`goodmem_rerankers_create`) for higher
   retrieval precision and an LLM (`goodmem_llms_create`) for answer
   summarization — both improve retrieval but neither is required to start.

## 3. Create a space

`goodmem_spaces_create` with a clear, human-readable name and the chosen
embedder. Name spaces after their content ("project-atlas-docs"), tell the user
which name you chose, and let them rename (`goodmem_spaces_update`).

## 4. Ingest memories

- Plain text or single facts → `goodmem_memories_create`.
- Many items at once → `goodmem_memories_batch_create` (one call, not a loop).
- PDF, DOCX, or scanned files → `goodmem_ocr_document` (a GoodMem Enterprise
  feature; if unavailable on this instance, fall back to extracting text and
  ingesting it).

**Ingestion is asynchronous.** Embedding happens in the background: poll the
memory with `goodmem_memories_get` until its processing status is `COMPLETED`
before retrieving against it. Report progress on large batches rather than
polling silently for a long time.

## 5. Retrieve

`goodmem_memories_retrieve` is the primary tool:

- Scope with space IDs. If the user's intent doesn't clearly select a space,
  search across all visible spaces rather than asking.
- Narrow with a metadata filter expression when the user constrains by
  attributes ("only last year's reports") — filter on document metadata instead
  of hoping the query embeds those constraints.
- Default to retrieving source chunks and analyzing them yourself. Request
  server-side answer summarization only when the user wants a direct sourced
  answer and the extra latency is acceptable — it invokes an LLM and runs
  longer.
- To read a full memory behind a search hit: `goodmem_memories_get` for the
  record, `goodmem_memories_content` for the original content, and
  `goodmem_memories_pages` for page-level access to ingested documents.

## 6. Recover from structured errors

Retrieval tools return structured, repairable errors — read them and
self-correct instead of surfacing raw errors to the user:

| Error code | Meaning | Recovery |
|---|---|---|
| `SPACE_SELECTION_REQUIRED` | Multiple (or zero) visible spaces, none selected | Pick from the listed spaces (or create one) and retry |
| `RERANKER_SELECTION_REQUIRED` | Ambiguous reranker choice | Pass an explicit reranker, or none to skip reranking |
| `LLM_SELECTION_REQUIRED` | Summarization requested but no LLM selectable | Pass an explicit LLM, or retrieve without summarization |

## 7. Housekeeping rules

- Deleting is destructive: confirm with the user before `goodmem_memories_delete`
  or any `*_delete` tool, and never bulk-delete by looping without an explicit
  instruction covering the whole set.
- Keep tool output out of the user's face: summarize retrieval results with
  citations to memory IDs; don't dump raw chunks unless asked.
- Administrative tools (API keys, system, admin namespaces) are for operators:
  use them only when the user explicitly asks for that operation.
