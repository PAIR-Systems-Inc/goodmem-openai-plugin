<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.create

```java
RerankerResponse create(RerankerCreationRequest request)
```

Create a new reranker

Creates a new reranker configuration for ranking search results. Rerankers represent connections to different reranking API services (like TEI, OpenAI, etc.) and include all the necessary configuration to use them for result ranking.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another reranker exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison.

DEFAULTS: apiPath defaults to '/v2/rerank' for Cohere and '/rerank' for other providers if omitted; supportedModalities defaults to [TEXT] if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_RERANKER is evaluated against the proposed reranker and owner. This operation is NOT idempotent - each request creates a new reranker record.

```java
RerankerResponse create(RerankerCreationRequest request, String apiKey)
```

Convenience overload: auto-fills provider / endpoint / dimensionality
 from the bundled model registry keyed by `modelIdentifier`,
 and converts a bare `apiKey` string to the structured
 `EndpointAuthentication`. Pass `null` for
 `apiKey` to preserve `request.credentials()`.
 Any field already set on `request` wins over registry values.

[rerankers](../rerankers.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RerankerCreationRequest](../models/RerankerCreationRequest.md)
