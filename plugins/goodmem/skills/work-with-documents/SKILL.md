---
name: work-with-documents
description: Save original file attachments in GoodMem and later search, quote, compare, or navigate their contents. Use when the user asks to remember a shared file or work with a document already stored in GoodMem.
---

# Work with documents in GoodMem

When the user asks to save a PDF or another uploaded file, send the original file
to GoodMem. GoodMem preserves its bytes and handles extraction and chunking.
Create one memory per original file, not one memory per page. Reading or
transcribing the attachment first is unnecessary and loses its original structure.

## Ingest a shared document

1. Call `goodmem_spaces_list`; reuse the matching space or create a topic-based
   one. Tell the user which space you used.
2. Call `goodmem_memories_upload` with the selected `space_id`, a unique
   `operation_id`, and the attachment's native `file` object: `download_url` and
   `file_id`, plus `file_name` and `mime_type` when available. Do not pass base64,
   a local path, or extracted page text to the text-create tool.
3. Include metadata such as `{"type":"document","filename":"<original name>"}`
   and the context it was shared for. Set `extract_page_images=true` when PDF
   page images should also be retained; separate per-page uploads are unnecessary.
4. After an interrupted response, retry with the same operation ID, file ID,
   and other arguments. Refresh only an expired download URL. The gateway can
   recover an accepted file without uploading it again.
5. Keep ingesting without polling every file. Check the space in bulk with
   `goodmem_memories_list`, then apply the processing and failure rules from
   `using-goodmem-memory`.

Follow the file-size limit advertised by the upload tool. If a known size exceeds
it, ask for a smaller file or a split original document. If size is unknown, try
the upload and explain any size-limit rejection without retrying the unchanged file.

If `goodmem_memories_upload` or a usable native file object is unavailable, explain
that original-file upload is unavailable on this connection. Check for updated
tools or request a fresh attachment; do not invent a download URL or silently
switch to transcription. Use `goodmem_memories_create` for pasted text, notes, or
excerpts only when the user asks to save that text. Split those text saves at
natural boundaries when useful, preserving source and page metadata.

An upload by itself is not permission to retain the file indefinitely. Save it to
GoodMem when the user asks to remember, add, store, or ingest it; otherwise work
with the upload only for the current request.

## Work with stored documents

- Retrieve passages with `goodmem_memories_retrieve`; use `metadata_filter` when
  the user identifies a filename, type, or other stored attribute.
- Read stored text with `goodmem_memories_content`. When `truncated` is true,
  continue with the returned `next_offset` until the needed text is read.
  Offsets count UTF-8 bytes; use the returned value rather than a character
  count. The native `fetch` tool returns the first page; when `truncated` is true,
  continue with `goodmem_memories_content`, setting `memory_id` to the returned
  `id` and `offset` to `next_offset`. `fetch` itself does not accept an offset.
  For binary originals such as PDFs, use retrieved text passages and page
  metadata; do not present the original binary bytes as extracted text.
- Use `goodmem_memories_pages` to list retained page images. It does not upload
  pages or replace the original-file upload.
- Use `goodmem_memories_list` to see what a space contains.

Quote or paraphrase the relied-on passage and name its filename. When comparing
documents, attribute each claim and describe disagreements explicitly.

An original-file upload has one memory ID; older text ingestions may have several
parts. Confirm the document and scope before calling `goodmem_memories_delete`
on the relevant memory IDs.
