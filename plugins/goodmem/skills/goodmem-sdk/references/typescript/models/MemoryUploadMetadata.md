<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryUploadMetadata

```ts

export type MemoryUploadMetadata = MemoryCreateMetadata;
```

Effective request fields (including inherited fields and overrides):

- `chunkingConfig` (`ChunkingConfiguration | null | undefined`, optional): Chunking strategy for this memory (if not provided, uses space default)
- `extractPageImages` (`boolean | null | undefined`, optional): Optional hint to extract page images for eligible document types (for example, PDFs)
- `memoryId` (`string | null | undefined`, optional): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use.
- `metadata` (`Record<string, unknown> | null | undefined`, optional): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks.
- `originalContentRef` (`string | null | undefined`, optional): Reference to external content location
- `spaceId` (`string`, required): ID of the space where this memory will be stored

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [MemoryCreateMetadata](MemoryCreateMetadata.md)
