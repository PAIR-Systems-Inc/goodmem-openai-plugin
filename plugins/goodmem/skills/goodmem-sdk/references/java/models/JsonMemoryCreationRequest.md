<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# JsonMemoryCreationRequest

Request body for creating a new Memory. A Memory represents content stored in a space.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `memoryId` (`MemoryId`): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use. Typed wrapper `MemoryId`; build from a raw string with `MemoryId.from(String)`.
- `spaceId` (`SpaceId`): ID of the space where this memory will be stored. Typed wrapper `SpaceId`; build from a raw string with `SpaceId.from(String)`.
- `originalContent` (`String`): Original content as plain text (use either this or originalContentB64)
- `originalContentB64` (`String`): Original content as base64-encoded binary data (use either this or originalContent)
- `originalContentRef` (`String`): Reference to external content location
- `contentType` (`String`): MIME type of the content
- `metadata` (`java.util.Map<String, Object>`): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks.
- `chunkingConfig` (`ChunkingConfiguration`): Chunking strategy for this memory (if not provided, uses space default)
- `extractPageImages` (`Boolean`): Optional hint to extract page images for eligible document types (for example, PDFs)
- `fileField` (`String`): Optional multipart file field name to bind binary content; required when multiple files are uploaded in a batch multipart request.

[Java](../../java.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [MemoryId](MemoryId.md)
- [SpaceId](SpaceId.md)
