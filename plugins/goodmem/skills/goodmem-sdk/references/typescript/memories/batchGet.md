<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.batchGet

Retrieves multiple memories in a single operation, with individual success/failure results. Each item requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```ts
batchGet(request: BatchMemoryRetrievalRequest, requestOptions?: RequestOptions): Promise<BatchMemoryResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [BatchMemoryRetrievalRequest](../models/BatchMemoryRetrievalRequest.md)
- [RequestOptions](../models/RequestOptions.md)
