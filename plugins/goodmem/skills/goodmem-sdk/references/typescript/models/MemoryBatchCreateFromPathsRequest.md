<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryBatchCreateFromPathsRequest

```ts

export type MemoryBatchCreateFromPathsRequest = Prettify<{
    requests: [MemoryCreateFromPathRequest, ...MemoryCreateFromPathRequest[]];
}>;
```

Effective request fields (including inherited fields and overrides):

- `requests` (`[{ memoryId?: string | null | undefined; spaceId: string; originalContentRef?: string | null | undefined; metadata?: (Record<string, unknown> | null) | undefined; chunkingConfig?: (ChunkingConfiguration | null) | undefined; extractPageImages?: boolean | null | undefined; path: string | URL; contentType?: string | null | undefined; filename?: string | null | undefined; }, ...{ memoryId?: string | null | undefined; spaceId: string; originalContentRef?: string | null | undefined; metadata?: (Record<string, unknown> | null) | undefined; chunkingConfig?: (ChunkingConfiguration | null) | undefined; extractPageImages?: boolean | null | undefined; path: string | URL; contentType?: string | null | undefined; filename?: string | null | undefined; }[]]`, required):

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [MemoryCreateFromPathRequest](MemoryCreateFromPathRequest.md)
