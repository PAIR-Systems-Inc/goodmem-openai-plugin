<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.list

Lists all memories within a given space. Pagination is supported via maxResults and nextToken (opaque). nextToken is a URL-safe Base64 string without padding; do not parse or construct it. This is a read-only operation with no side effects and is safe to retry.

AUTHORIZATION: Requires LIST_MEMORY on the exact containing space. Each returned memory must also satisfy READ_MEMORY, either directly or through DIRECT_MEMBERS_OF that space. Both predicates are evaluated in PostgreSQL. Returns NOT_FOUND if the specified space does not exist.

```ts
list(spaceId: string, options?: MemoriesListOptions, requestOptions?: RequestOptions): Promise<Page<MemoryResponseShape>>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesListOptions](../models/MemoriesListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
