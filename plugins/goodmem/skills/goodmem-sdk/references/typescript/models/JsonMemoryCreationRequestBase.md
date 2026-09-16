<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# JsonMemoryCreationRequestBase

- `memoryId` (`string | null`, optional): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use.
- `spaceId` (`string`, required): ID of the space where this memory will be stored
- `originalContent` (`string | null`, optional): Original content as plain text (use either this or originalContentB64)
- `originalContentB64` (`string | null`, optional): Original content as base64-encoded binary data (use either this or originalContent)
- `originalContentRef` (`string | null`, optional): Reference to external content location
- `contentType` (`string`, required): MIME type of the content
- `metadata` (`Record<string, unknown> | null`, optional): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks.
- `chunkingConfig` (`ChunkingConfiguration | null`, optional): Chunking strategy for this memory (if not provided, uses space default)
- `extractPageImages` (`boolean | null`, optional): Optional hint to extract page images for eligible document types (for example, PDFs)
- `fileField` (`string | null`, optional): Optional multipart file field name to bind binary content; required when multiple files are uploaded in a batch multipart request.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
