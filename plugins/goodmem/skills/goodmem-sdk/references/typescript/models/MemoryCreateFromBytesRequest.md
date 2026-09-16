<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryCreateFromBytesRequest

```ts

export type MemoryCreateFromBytesRequest = Prettify<MemoryUploadMetadata & {
    bytes: Uint8Array | ArrayBuffer;
    contentType: string;
    filename?: string | null;
}>;
```

Effective request fields (including inherited fields and overrides):

- `bytes` (`ArrayBuffer | Uint8Array<ArrayBufferLike>`, required):
- `chunkingConfig` (`ChunkingConfiguration | null | undefined`, optional): Chunking strategy for this memory (if not provided, uses space default)
- `contentType` (`string`, required):
- `extractPageImages` (`boolean | null | undefined`, optional): Optional hint to extract page images for eligible document types (for example, PDFs)
- `filename` (`string | null | undefined`, optional):
- `memoryId` (`string | null | undefined`, optional): Optional client-provided UUID for the memory. If omitted, the server generates one. Returns ALREADY_EXISTS if the ID is already in use.
- `metadata` (`Record<string, unknown> | null | undefined`, optional): Additional metadata for the memory. A top-level textual title is an optional document-title hint for embedding providers that support one; blank or non-string titles are ignored. Later metadata edits do not automatically re-embed existing chunks.
- `originalContentRef` (`string | null | undefined`, optional): Reference to external content location
- `spaceId` (`string`, required): ID of the space where this memory will be stored

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [MemoryUploadMetadata](MemoryUploadMetadata.md)
