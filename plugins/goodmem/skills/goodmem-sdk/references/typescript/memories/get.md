<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.get

Retrieves a single memory by its ID.

AUTHORIZATION: Requires READ_MEMORY on the requested memory; authority may be granted directly or through DIRECT_MEMBERS_OF its containing space. This is a read-only operation with no side effects and is safe to retry. Returns NOT_FOUND if the memory or its parent space does not exist.

```ts
get(id: string, options?: MemoriesGetOptions, requestOptions?: RequestOptions): Promise<MemoryResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesGetOptions](../models/MemoriesGetOptions.md)
- [RequestOptions](../models/RequestOptions.md)
