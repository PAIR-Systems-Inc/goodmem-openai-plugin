<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# rerankers.list

List rerankers

Retrieves a list of reranker configurations accessible to the caller, with optional filtering.

IMPORTANT: Pagination is NOT supported - all matching results are returned. Results are ordered by created_at descending. Stored credentials are never included in list responses.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_RERANKER on the GoodMem instance. Each returned reranker must also be visible through READ_RERANKER; unauthorized rerankers are filtered in PostgreSQL. The owner_id parameter filters that already-authorized result set and does not grant additional visibility.

Args:
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).
    owner_id (str, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-reranker READ_RERANKER filtering.
    provider_type (ProviderType, optional): Filter rerankers by provider type. Allowed values match the ProviderType schema.

Returns:
    list[RerankerResponse]

```python
rerankers.list(*, label: 'dict[str, str] | None' = None, owner_id: 'str | None' = None, provider_type: 'ProviderType | None' = None) -> 'list[RerankerResponse]'
```

[rerankers](../rerankers.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [ProviderType](../models/ProviderType.md)
