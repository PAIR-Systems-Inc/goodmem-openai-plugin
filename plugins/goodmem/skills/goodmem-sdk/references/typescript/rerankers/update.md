<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# rerankers.update

Updates an existing reranker configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

IMMUTABLE FIELDS: providerType and ownerId cannot be changed after creation.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself. Returns ALREADY_EXISTS if update would create an equivalent reranker configuration for this owner after endpoint canonicalization and provider-default resolution (HTTP 409 Conflict / ALREADY_EXISTS). Requires UPDATE_RERANKER on the requested reranker. This operation is idempotent.

```ts
update(id: string, request: UpdateRerankerRequest, requestOptions?: RequestOptions): Promise<RerankerResponseShape>
```

[rerankers](../rerankers.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateRerankerRequest](../models/UpdateRerankerRequest.md)
