<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.create

Create a new memory

Create a memory from text content, base64-encoded content, or a local file. Content must be provided via exactly one of `file_path`, `original_content`, or `original_content_b64`. `original_content_ref` is a metadata pointer (URL) attached to the memory; it does NOT supply content and may accompany the chosen content source.

Args:
    space_id (str): ID of the space where this memory will be stored
    chunking_config (ChunkingConfiguration, optional): Chunking strategy for this memory (if not provided, uses space default)
    content_type (str, optional): MIME type of the content. Auto-inferred as `"text/plain"` for `original_content`, or from the file extension for `file_path`. Required when using `original_content_b64` (the server cannot infer MIME type from base64 bytes). NOT required for `original_content_ref` — ref is a metadata pointer, not a content source.
    extract_page_images (bool, optional): Optional hint to extract page images for eligible document types (for example, PDFs)
    memory_id (str, optional): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use.
    metadata (dict[str, Any], optional): Metadata for the memory. Any JSON-serializable dict. Can be nested. Can be used for filtering in memory list operation. (e.g. `{"author": "John Doe", "tags": ["production", "urgent"]}`)
    original_content (str, optional): Original content as plain text. Mutually exclusive with `file_path` and `original_content_b64`.
    original_content_b64 (str, optional): Original content as base64-encoded binary data. Mutually exclusive with `file_path` and `original_content`.
    original_content_ref (str, optional): Reference to external content location. Functions as a metadata field. Does not make Goodmem download the content from the URL and use it to create memory.
    file_path (str, optional): Local file path — the SDK reads and uploads via multipart.

Returns:
    Memory

```python
memories.create(*, space_id: 'str', chunking_config: 'ChunkingConfiguration | None' = None, content_type: 'str | None' = None, extract_page_images: 'bool | None' = None, memory_id: 'str | None' = None, metadata: 'dict[str, Any] | None' = None, original_content: 'str | None' = None, original_content_b64: 'str | None' = None, original_content_ref: 'str | None' = None, file_path: 'str | None' = None) -> 'Memory'
```

[memories](../memories.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](../models/ChunkingConfiguration.md)
