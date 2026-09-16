<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# MemoryCreationRequest

Convenience version — ``content_type`` is optional (auto-inferred for text).

Identical to the generated ``MemoryCreationRequest`` except ``content_type``
defaults to ``None``.  When passed to ``batch_create``, the SDK infers
``"text/plain"`` when ``original_content`` is a string and no explicit
``content_type`` is provided.

```python
from goodmem import MemoryCreationRequest
```

- `memory_id` (`str | None`, optional): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use. JSON: `memoryId`.
- `space_id` (`str`, required): ID of the space where this memory will be stored JSON: `spaceId`.
- `original_content` (`str | None`, optional): Original content as plain text (use either this or original_content_b64) JSON: `originalContent`.
- `original_content_b64` (`str | None`, optional): Original content as base64-encoded binary data (use either this or original_content) JSON: `originalContentB64`.
- `original_content_ref` (`str | None`, optional): Reference to external content location JSON: `originalContentRef`.
- `content_type` (`Annotated[str, strict=True] | None`, optional): MIME type of the content. Auto-inferred as 'text/plain' when original_content is a string. JSON: `contentType`.
- `metadata` (`dict[str, Any] | None`, optional): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks.
- `chunking_config` (`ChunkingConfiguration | None`, optional): Chunking strategy for this memory (if not provided, uses space default) JSON: `chunkingConfig`.
- `extract_page_images` (`bool | None`, optional): Optional hint to extract page images for eligible document types (for example, PDFs) JSON: `extractPageImages`.
- `file_field` (`str | None`, optional): Optional multipart file field name to bind binary content; required when multiple files are uploaded in a batch multipart request. JSON: `fileField`.

[Python](../../python.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
