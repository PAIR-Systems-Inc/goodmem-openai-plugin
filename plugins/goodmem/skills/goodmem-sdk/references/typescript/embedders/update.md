<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# embedders.update

Updates explicitly supplied embedder fields; at least one mutable field is required. Field omission and reset semantics are defined by the request schema, and providerType cannot be changed. Returns 409 if the resulting configuration duplicates another embedder for the owner, and 412 when model-defining fields are changed while the embedder is in use. Requires UPDATE_EMBEDDER on the requested embedder. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

```ts
update(id: string, request: UpdateEmbedderRequest, requestOptions?: RequestOptions): Promise<EmbedderResponseShape>
```

[embedders](../embedders.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateEmbedderRequest](../models/UpdateEmbedderRequest.md)
