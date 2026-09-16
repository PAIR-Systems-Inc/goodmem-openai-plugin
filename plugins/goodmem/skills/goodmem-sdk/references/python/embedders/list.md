<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# embedders.list

List embedders

Retrieves a list of embedder configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_EMBEDDER on the GoodMem instance. Each returned embedder must also be visible through READ_EMBEDDER; unauthorized embedders are filtered in PostgreSQL. The owner_id parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

Args:
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).
    owner_id (str, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-embedder READ_EMBEDDER filtering.
    provider_type (ProviderType, optional): Filter embedders by provider type. Allowed values match the ProviderType schema.

Returns:
    list[EmbedderResponse]

```python
embedders.list(*, label: 'dict[str, str] | None' = None, owner_id: 'str | None' = None, provider_type: 'ProviderType | None' = None) -> 'list[EmbedderResponse]'
```

[embedders](../embedders.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [ProviderType](../models/ProviderType.md)
