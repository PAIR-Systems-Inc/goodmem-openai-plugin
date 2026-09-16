<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# JsonMemoryCreationRequest

Request body for creating a new Memory. A Memory represents content stored in a space.

`Goodmem.Client.Models.JsonMemoryCreationRequest`

- `ChunkingConfig` (`ChunkingConfiguration?`): Chunking strategy for this memory (if not provided, uses space default) JSON: `chunkingConfig`.
- `ContentType` (`string?`): MIME type of the content JSON: `contentType`.
- `ExtractPageImages` (`bool?`): Optional hint to extract page images for eligible document types (for example, PDFs) JSON: `extractPageImages`.
- `FileField` (`string?`): Optional multipart file field name to bind binary content; required when multiple files are uploaded in a batch multipart request. JSON: `fileField`.
- `MemoryId` (`string?`): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use. JSON: `memoryId`.
- `Metadata` (`IReadOnlyDictionary<string, object>?`): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks. JSON: `metadata`.
- `OriginalContent` (`string?`): Original content as plain text (use either this or originalContentB64) JSON: `originalContent`.
- `OriginalContentB64` (`string?`): Original content as base64-encoded binary data (use either this or originalContent) JSON: `originalContentB64`.
- `OriginalContentRef` (`string?`): Reference to external content location JSON: `originalContentRef`.
- `SpaceId` (`string`, required): ID of the space where this memory will be stored JSON: `spaceId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
