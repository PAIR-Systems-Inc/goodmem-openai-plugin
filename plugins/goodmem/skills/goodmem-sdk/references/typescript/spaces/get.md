<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.get

Retrieves a specific space by its unique identifier. Returns the complete space information, including name, labels, embedder configuration, and metadata. Requires READ_SPACE on the requested space. The service distinguishes a missing space from an existing space the caller cannot read. This is a read-only operation safe to retry.

```ts
get(id: string, requestOptions?: RequestOptions): Promise<SpaceResponseShape>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
