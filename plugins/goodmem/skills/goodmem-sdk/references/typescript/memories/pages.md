<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.pages

Lists extracted page-image metadata for a memory with optional filters and pagination. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```ts
pages(id: string, options?: MemoriesPagesOptions, requestOptions?: RequestOptions): Promise<Page<MemoryPageImageResponseShape>>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesPagesOptions](../models/MemoriesPagesOptions.md)
- [RequestOptions](../models/RequestOptions.md)
