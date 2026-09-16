<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.batchDelete

Deletes memories using selector entries. Each selector can target either a specific memory ID or a filtered subset scoped to a specific space. Each selected memory requires DELETE_MEMORY; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```ts
batchDelete(request: BatchMemoryDeletionRequest, requestOptions?: RequestOptions): Promise<BatchMemoryResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [BatchMemoryDeletionRequest](../models/BatchMemoryDeletionRequest.md)
- [RequestOptions](../models/RequestOptions.md)
