<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.content

Returns the original binary payload for a memory. The response uses the memory's stored content type when available. Returns 404 when the memory does not have inline content; clients can check originalContentRef from the metadata endpoint to locate external content. Requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```ts
content(id: string, requestOptions?: RequestOptions): Promise<Uint8Array>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
