<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryBatchCreateFromFilesRequest

```ts

export type MemoryBatchCreateFromFilesRequest = Prettify<{
    requests: [MemoryCreateFromFileRequest, ...MemoryCreateFromFileRequest[]];
}>;
```

Effective request fields (including inherited fields and overrides):

- `requests` (`[{ memoryId?: string | null | undefined; spaceId: string; originalContentRef?: string | null | undefined; metadata?: (Record<string, unknown> | null) | undefined; chunkingConfig?: (ChunkingConfiguration | null) | undefined; extractPageImages?: boolean | null | undefined; file: Blob; contentType?: string | null | undefined; filename?: string | null | undefined; }, ...{ memoryId?: string | null | undefined; spaceId: string; originalContentRef?: string | null | undefined; metadata?: (Record<string, unknown> | null) | undefined; chunkingConfig?: (ChunkingConfiguration | null) | undefined; extractPageImages?: boolean | null | undefined; file: Blob; contentType?: string | null | undefined; filename?: string | null | undefined; }[]]`, required):

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [MemoryCreateFromFileRequest](MemoryCreateFromFileRequest.md)
