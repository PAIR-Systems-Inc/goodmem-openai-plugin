---
name: using-goodmem-memory
description: Recall, store, and manage knowledge in the user's GoodMem Cloud instance, and add or configure its models. Use when stored project or team knowledge may answer a question, when the user asks to save or organize knowledge, or when they ask to create, add, or set up an embedder, embedding model, reranker, or LLM on GoodMem — model setup is a one-time console link, never code. Use the SDK skill only when the user explicitly asks to write code.
---

# Using GoodMem memory

Treat GoodMem as the user's persistent project or team memory. The connection is
always through GoodMem's hosted gateway to the GoodMem Cloud instance selected
during sign-in. Never ask for an instance URL, API key, or local GoodMem server.

## Recall relevant knowledge

When stored decisions, notes, documents, project context, or earlier conversations
could plausibly answer the user's question, call `goodmem_memories_retrieve`
without asking permission first. Skip retrieval for general knowledge, arithmetic,
or questions fully answered by the current conversation.

- Scope to `space_ids` when the relevant space is clear. Otherwise search all
  spaces; use `goodmem_spaces_list` when seeing their names would help.
- Use `metadata_filter` for constraints represented by metadata, such as filename,
  type, topic, or year.
- Use `answer: true` when synthesis across many memories would materially help.
  Otherwise retrieve passages and answer from them directly.
- Report `warnings` and `skipped_spaces` when retrieval is partial. If
  `synthesis_error` is present, answer from the usable passages and explain the
  limitation. Per-space fallback interleaves local rankings; do not interpret
  its scores as one global relevance order.
- Name the source memory, document, or space. Prefer the user's retrieved record
  over general assumptions and call out conflicts.
- If nothing relevant is returned, say so plainly. Never invent a memory or imply
  that an unindexed memory appeared in search.

Use `goodmem_memories_content` for stored text, following `next_offset` while
`truncated` is true, and
`goodmem_memories_pages` to navigate page-oriented documents.

## Create and organize knowledge

Write only when the user asks to save, remember, ingest, or organize something.

1. Call `goodmem_spaces_list` and reuse an obviously matching space.
2. Otherwise call `goodmem_spaces_create` with a clear topic or project name and
   tell the user which space was chosen. The instance's embedder is selected
   automatically; if several exist, use an `embedder_name` offered by the tool.
3. Create one coherent memory per fact, passage, or natural section with useful
   typed metadata such as topic, source, filename, page, or date.

For conversations, follow the `save-conversation` skill. For files, follow the
`work-with-documents` skill.

If space creation reports that no embedder exists, relay its one-time setup link
exactly.

## Add or change models — embedder, reranker, LLM

On GoodMem, "create an LLM", "add an embedder", or "set up a reranker" means
registering a model configuration on the user's GoodMem Cloud instance. It is a
console action, identical on every surface:

1. Call `goodmem_console_setup` with `kind` set to `embedder`, `reranker`, or
   `llm`.
2. Relay the returned link verbatim, noting it works once, expires in about
   30 minutes, and asks for the user's own model provider API key on the page.
3. When the user says they are done, retry whatever needed the model.

Never write code, scaffold a project, or touch provider credentials for this —
the API key belongs on the console page, not in the chat. An embedder makes
memories searchable, a reranker sharpens retrieval order, and an LLM enables
synthesized answers. Write integration code only when the user explicitly asks
for code; then follow the `goodmem-sdk` skill.

## Processing and failures

Ingestion is asynchronous. Keep saving instead of polling after every memory.
A memory is searchable only at `COMPLETED`; do not describe `PENDING` or
`PROCESSING` content as searchable.

When a response reports `failed_count`, state how many memories failed. Use
`goodmem_memories_list` to inspect statuses and `goodmem_memories_get` when the
processing error is needed. Explain that model and provider-key repairs happen in
the GoodMem Cloud console. A `not_indexed` result means the content exists but is
not available to semantic search.

## Changes and deletion

Creating, updating, and deleting require user intent. Confirm the specific target
before `goodmem_memories_delete`; never loop over a whole space on a vague deletion
request. Keep raw tool output out of the response unless the user asks for it.
