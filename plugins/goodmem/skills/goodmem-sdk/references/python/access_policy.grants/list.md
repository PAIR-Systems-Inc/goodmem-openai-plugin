<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.grants.list

List authorization grants

Lists grants attached to one resource. MANAGE_ACCESS is required on that resource; continuation tokens are bound to the caller and filters.

Args:
    resource_kind (Literal['INSTANCE', 'USER', 'SERVICE_IDENTITY', 'SPACE', 'API_KEY', 'EMBEDDER', 'RERANKER', 'LLM', 'MEMORY', 'EXTENSION', 'RETRIEVE_MEMORY_LOG_POLICY']): Required target resource kind
    resource_id (str, optional): Required target UUID except when resource_kind is INSTANCE
    include_revoked (bool, optional, default=False): Include revoked history
    max_results (int, optional, default=50): Page size; 0 or omission uses the default of 50, maximum 1,000
    next_token (str, optional): Opaque continuation token

Returns:
    Page[AuthorizationGrant]

```python
access_policy.grants.list(*, resource_kind: "Literal['INSTANCE', 'USER', 'SERVICE_IDENTITY', 'SPACE', 'API_KEY', 'EMBEDDER', 'RERANKER', 'LLM', 'MEMORY', 'EXTENSION', 'RETRIEVE_MEMORY_LOG_POLICY']", resource_id: 'str | None' = None, include_revoked: 'bool | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[AuthorizationGrant]'
```

[access_policy.grants](../access_policy.grants.md) · [Python](../../python.md)
