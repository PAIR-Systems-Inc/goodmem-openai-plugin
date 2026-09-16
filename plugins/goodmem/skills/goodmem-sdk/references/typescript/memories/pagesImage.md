<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.pagesImage

Downloads inline bytes for one page image. The page index is required. The optional dpi and content type query parameters act as rendition filters; if omitted, the server returns the unique rendition for that page or rejects ambiguous matches. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```ts
pagesImage(id: string, pageIndex: number, options?: MemoriesPagesImageOptions, requestOptions?: RequestOptions): Promise<Uint8Array>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesPagesImageOptions](../models/MemoriesPagesImageOptions.md)
- [RequestOptions](../models/RequestOptions.md)
