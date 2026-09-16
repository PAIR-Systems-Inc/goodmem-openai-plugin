<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.batchCreate

Creates multiple memories in a single operation, with individual success/failure results. Each item requires CREATE_MEMORY on its containing space; authorization failures are reported in the corresponding item result.

```ts
batchCreate(request: MemoryBatchCreateRequest, requestOptions?: RequestOptions): Promise<BatchMemoryResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoryBatchCreateRequest](../models/MemoryBatchCreateRequest.md)
- [RequestOptions](../models/RequestOptions.md)
