<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# embedders.get

Retrieves the details of a specific embedder configuration by its unique identifier. Requires READ_EMBEDDER on the requested embedder. The service distinguishes a missing embedder from an existing embedder the caller cannot read. This is a read-only operation with no side effects.

```ts
get(id: string, options?: EmbeddersGetOptions, requestOptions?: RequestOptions): Promise<EmbedderResponseShape>
```

[embedders](../embedders.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbeddersGetOptions](../models/EmbeddersGetOptions.md)
- [RequestOptions](../models/RequestOptions.md)
