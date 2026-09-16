<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.update

Update a reranker

Updates an existing reranker configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

IMMUTABLE FIELDS: providerType and ownerId cannot be changed after creation.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself. Returns ALREADY_EXISTS if update would create an equivalent reranker configuration for this owner after endpoint canonicalization and provider-default resolution (HTTP 409 Conflict / ALREADY_EXISTS). Requires UPDATE_RERANKER on the requested reranker. This operation is idempotent.

```java
RerankerResponse update(String id, UpdateRerankerRequest request)
```

```java
RerankerResponse update(ai.pairsys.goodmem.client.models.RerankerId id, UpdateRerankerRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
RerankerResponse update(java.util.UUID id, UpdateRerankerRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[rerankers](../rerankers.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RerankerId](../models/RerankerId.md)
- [UpdateRerankerRequest](../models/UpdateRerankerRequest.md)
