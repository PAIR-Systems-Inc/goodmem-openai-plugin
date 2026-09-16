<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# rerankers.update

Update a reranker

Updates an existing reranker configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

IMMUTABLE FIELDS: provider_type and owner_id cannot be changed after creation.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself. Returns ALREADY_EXISTS if update would create an equivalent reranker configuration for this owner after endpoint canonicalization and provider-default resolution (HTTP 409 Conflict / ALREADY_EXISTS). Requires UPDATE_RERANKER on the requested reranker. This operation is idempotent.

Args:
    id (str): The unique identifier of the reranker to update
    request (UpdateRerankerRequest | dict): The request payload. Accepts a UpdateRerankerRequest instance or a plain dict with the same fields.

Returns:
    RerankerResponse

```python
rerankers.update(*, id: 'str', request: 'UpdateRerankerRequest | dict') -> 'RerankerResponse'
```

[rerankers](../rerankers.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateRerankerRequest](../models/UpdateRerankerRequest.md)
