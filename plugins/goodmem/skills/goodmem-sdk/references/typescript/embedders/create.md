<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# embedders.create

Creates an embedder configuration for use with memory spaces. If ownerId is omitted, the authenticated principal becomes the owner; CREATE_EMBEDDER is evaluated against that proposed embedder and owner. Returns 409 when an equivalent embedder configuration already exists for the owner. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

```ts
create(request: EmbeddersCreateKnownWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<EmbedderResponseShape>
create(request: EmbeddersCreateKnownWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<EmbedderResponseShape>
create(request: EmbeddersCreateCustomWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<EmbedderResponseShape>
create(request: EmbeddersCreateCustomWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<EmbedderResponseShape>
```

[embedders](../embedders.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbeddersCreateCustomWithCredentialsRequest](../models/EmbeddersCreateCustomWithCredentialsRequest.md)
- [EmbeddersCreateCustomWithoutCredentialsRequest](../models/EmbeddersCreateCustomWithoutCredentialsRequest.md)
- [EmbeddersCreateKnownWithCredentialsRequest](../models/EmbeddersCreateKnownWithCredentialsRequest.md)
- [EmbeddersCreateKnownWithoutCredentialsRequest](../models/EmbeddersCreateKnownWithoutCredentialsRequest.md)
- [ProviderApiKeyOptions](../models/ProviderApiKeyOptions.md)
- [ProviderNoApiKeyOptions](../models/ProviderNoApiKeyOptions.md)
