---
name: goodmem-memory-workflow
description: The end-to-end GoodMem memory workflow — create spaces, ingest text and documents, wait for processing, and retrieve with semantic search, metadata filters, and optional answer summarization. Use when the user wants to store knowledge, ingest files, or search memories.
---

# GoodMem Memory Workflow

GoodMem tools are named `goodmem_<namespace>_<action>` (for example
`goodmem_spaces_create`), plus the standard `search` and `fetch` pair. The
connection is to the user's GoodMem Cloud instance, already signed in — never
ask for URLs or API keys.

## 1. Find or create a space

A space is the container for related memories — one per project, team, or
topic.

1. `goodmem_spaces_list` first: prefer an existing space whose name matches
   the material over creating a near-duplicate.
2. Otherwise `goodmem_spaces_create` with a clear, human-readable name. The
   instance's embedder is selected automatically; if several exist, the
   error names the options — pass `embedder_name` from that list. Name spaces
   after their content ("project-atlas-docs"), tell the user which name you
   chose, and let them rename (`goodmem_spaces_update`).

If creation fails because the instance has no embedding model yet, the error
carries a one-time setup link: give the user the message and the link exactly
as instructed there, wait for them to finish, then retry.

## 2. Ingest memories

- Plain text or single facts → `goodmem_memories_create`, one call per
  memory. For many items, loop — one memory per call, each with its own
  metadata.
- Documents → GoodMem stores text, so the file never travels: read it
  yourself and save what you read. Transcribe the text faithfully, describe
  figures and images in words where they appear, and save the parts as
  separate memories at whatever granularity fits (per page, per section),
  each with metadata like `{"filename": ..., "page": ...}`. Save a whole
  document as one memory only if the user explicitly asks.
- Give every memory useful metadata (topic, source, date): metadata values
  can be any JSON — numbers and booleans stay typed, so `{"seq": 5}` can be
  filtered numerically later.

**Ingestion is asynchronous and does not block you.** Keep saving; never pause
to poll each memory. Check in bulk instead: `goodmem_memories_list` returns
`processing_status` for up to 500 memories per call (pass `all: true` to walk
a larger space; a `truncated` flag tells you when there is more) — check once
partway through a long ingestion and once at the end.

**Report failure, not success.** If any row is `FAILED`, call
`goodmem_memories_get` on that memory to read `processing_error` and tell the
user plainly what is broken (for example an embedding model whose provider key
is no longer valid) and that the fix is in their GoodMem console. Do not
narrate healthy processing. Before retrieving, confirm the rows you need are
`COMPLETED`.

## 3. Retrieve

- Semantic search → `goodmem_memories_retrieve` with a natural-language
  message and the space ids to search. Results carry relevance scores and
  memory ids.
- Narrow with `metadata_filter` when the user names a document or topic that
  ingestion stored as metadata.
- Direct questions → pass `answer: true` to have an LLM summarize the
  retrieved memories into an answer; cite the memory ids you used.
- Whole memory back → `goodmem_memories_content`.
- `search` / `fetch` are the standard wrappers over the same retrieval — use
  the goodmem-prefixed tools when you need scores, filters, or summarization.

## 4. Housekeeping rules

- Deleting is destructive: confirm with the user before
  `goodmem_memories_delete`, and never bulk-delete by looping without an
  explicit instruction covering the whole set.
- Keep tool output out of the user's face: summarize retrieval results with
  citations to memory ids; don't dump raw chunks unless asked.
- The instance's model catalog is read-only here: `goodmem_embedders_list`,
  `goodmem_rerankers_list`, and `goodmem_llms_list` show what's configured.
  Provisioning or changing models, API keys, users, and access policy happens
  in the GoodMem Cloud console — when the user asks for those, direct them
  there.
