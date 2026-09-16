<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.retrieve

Streams semantic retrieval results with full feature support including context items and embedder weight overrides, per-space filters, and request-level HNSW tuning.

AUTHORIZATION: Every requested space must grant LIST_MEMORY on that exact space and READ_MEMORY through DIRECT_MEMBERS_OF the space before retrieval begins.

```ts
retrieve(request: MemoriesRetrieveParams, requestOptions?: RequestOptions): AsyncIterable<RetrieveMemoryEventResponseShape>
retrieve(message: string, options: MemoriesRetrieveOptions, requestOptions?: RequestOptions): AsyncIterable<RetrieveMemoryEventResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesRetrieveOptions](../models/MemoriesRetrieveOptions.md)
- [MemoriesRetrieveParams](../models/MemoriesRetrieveParams.md)
- [RequestOptions](../models/RequestOptions.md)
