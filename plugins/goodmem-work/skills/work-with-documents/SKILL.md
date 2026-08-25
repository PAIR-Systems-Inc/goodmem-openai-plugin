---
name: work-with-documents
description: Put documents into GoodMem and work with them afterwards — ingest uploaded or pasted files into a space, then search, quote, and navigate them. Use when the user shares a document to remember, asks to add files to their memory, or asks about a document they stored earlier.
---

# Working with documents in GoodMem

## Ingesting a document the user shares

When the user uploads or pastes a document and wants it kept:

1. **Pick the space.** `goodmem_spaces_list`; reuse the matching one or create
   a space named for the document set ("supplier-contracts", "product-specs").
   Tell the user which space you used.
2. **Save the text you can read.** Use `goodmem_memories_create` with the
   document's extracted text. A memory holds text — do not store a filename or
   a link and consider the document saved.
3. **Always attach metadata**, because it is what makes later filtering work:
   `{"filename": "<original name>", "type": "document"}`, plus
   `{"context": "<why it was shared>"}` when there is a reason worth keeping.
4. **Split long documents** at natural boundaries (sections, chapters), one
   memory per part, each carrying the same `filename` and a `part` marker like
   `"3 of 7"`. Prefer several coherent memories over one enormous one.
5. **You are the document reader, and an upload alone is the request.** There
   is no OCR tool — read the attached file yourself, without waiting for the
   user to spell out what to do. Transcribe the text faithfully, and where a
   page carries a figure, photo, chart, or diagram, describe it in words where
   it appears (e.g. `[Figure: bar chart comparing Q1–Q4 revenue; Q3 highest]`).
   Save the parts as separate memories however fits the material — per page,
   per section, or one memory per image description — as you see fit; save the
   whole document as a single memory only if the user explicitly asks. If a
   page is truly illegible, say so plainly and save what you could read rather
   than silently dropping it.
6. **Keep ingesting, and check in bulk.** Processing runs in the background
   and does not block saving, so never pause between parts and never poll
   each memory in turn. Instead call `goodmem_memories_list` on the space —
   it returns `processing_status` for every memory in a single call, however
   many there are — once partway through a long ingestion and once at the
   end.
7. **Speak up only when something failed.** If any row is `FAILED`, call
   `goodmem_memories_get` on that memory to read `processing_error`, and tell
   the user plainly what is broken (for example an embedding model whose
   provider key is no longer valid) and that the fix is in their GoodMem
   console. Say nothing about processing when it is going fine — report the
   document is searchable once the rows you need are `COMPLETED`.

## Working with stored documents afterwards

- **Find passages:** `goodmem_memories_retrieve`, narrowing with
  `metadata_filter` on `filename` or `type` when the user names a document.
- **Read the whole thing:** `goodmem_memories_content`.
- **Navigate pages:** `goodmem_memories_pages` for documents ingested page by
  page — useful for "what does page 4 say".
- **See what a space holds:** `goodmem_memories_list`.

## Answer quality

Quote the passage you relied on and name its filename. When a user asks a
question that spans several documents, retrieve first, then compare the sources
explicitly ("the 2026 contract says X, while the operations checklist says Y").

## Housekeeping

Removing a document means deleting its memories — confirm which document, then
`goodmem_memories_delete` for each part. Never delete a whole space's contents
on a vague instruction.
