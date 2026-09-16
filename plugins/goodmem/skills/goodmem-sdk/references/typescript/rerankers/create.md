<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# rerankers.create

Creates a new reranker configuration for ranking search results. Rerankers represent connections to different reranking API services (like TEI, OpenAI, etc.) and include all the necessary configuration to use them for result ranking.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another reranker exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison.

DEFAULTS: apiPath defaults to '/v2/rerank' for Cohere and '/rerank' for other providers if omitted; supportedModalities defaults to [TEXT] if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_RERANKER is evaluated against the proposed reranker and owner. This operation is NOT idempotent - each request creates a new reranker record.

```ts
create(request: RerankersCreateKnownWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<RerankerResponseShape>
create(request: RerankersCreateKnownWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<RerankerResponseShape>
create(request: RerankersCreateCustomWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<RerankerResponseShape>
create(request: RerankersCreateCustomWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<RerankerResponseShape>
```

[rerankers](../rerankers.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ProviderApiKeyOptions](../models/ProviderApiKeyOptions.md)
- [ProviderNoApiKeyOptions](../models/ProviderNoApiKeyOptions.md)
- [RerankersCreateCustomWithCredentialsRequest](../models/RerankersCreateCustomWithCredentialsRequest.md)
- [RerankersCreateCustomWithoutCredentialsRequest](../models/RerankersCreateCustomWithoutCredentialsRequest.md)
- [RerankersCreateKnownWithCredentialsRequest](../models/RerankersCreateKnownWithCredentialsRequest.md)
- [RerankersCreateKnownWithoutCredentialsRequest](../models/RerankersCreateKnownWithoutCredentialsRequest.md)
