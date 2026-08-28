---
name: work-with-documents
description: Save readable document content in GoodMem and later search, quote, compare, or navigate it. Use when the user asks to remember a shared file or work with a document already stored in GoodMem.
---

# Work with documents in GoodMem

GoodMem stores searchable text. When the user asks to remember a file, read the
file and save its contents; a filename, path, or link alone is not ingestion.

## Ingest a shared document

1. Call `goodmem_spaces_list`; reuse the matching space or create a topic-based
   one. Tell the user which space you used.
2. Read or extract the document faithfully. Transcribe scanned text and describe
   meaningful figures, photographs, charts, and diagrams in words where they
   appear. If something is illegible, identify what could not be read.
3. Split long material at natural section, chapter, or page boundaries. Prefer
   coherent parts; save the whole document as one memory only when explicitly
   requested or when it is already short.
4. Call `goodmem_memories_create` for each part with metadata including
   `{"type":"document","filename":"<original name>"}`. Add context, page, topic,
   and a marker such as `"part":"2 of 5"` where useful.
5. Keep ingesting without polling every part. Check the space in bulk with
   `goodmem_memories_list`, then apply the processing and failure rules from
   `using-goodmem-memory`.

An upload by itself is not permission to retain the file indefinitely. Save it to
GoodMem when the user asks to remember, add, store, or ingest it; otherwise work
with the upload only for the current request.

## Work with stored documents

- Retrieve passages with `goodmem_memories_retrieve`; use `metadata_filter` when
  the user identifies a filename, type, or other stored attribute.
- Read a full stored memory with `goodmem_memories_content`.
- Use `goodmem_memories_pages` for page-oriented ingestion.
- Use `goodmem_memories_list` to see what a space contains.

Quote or paraphrase the relied-on passage and name its filename. When comparing
documents, attribute each claim and describe disagreements explicitly.

Removing a document means deleting all of its memory parts. Confirm the document
and scope before calling `goodmem_memories_delete` for those parts.
