<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# service_identities.list

List service identities

Requires LIST_SERVICE_IDENTITY on the GoodMem instance and READ_SERVICE_IDENTITY on each returned row. Owner and label filters, lifecycle filtering, authorization, and keyset pagination execute in PostgreSQL.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Args:
    owner_principal_id (str, optional): Exact current administrative-owner principal UUID
    include_deleted (bool, optional, default=False): Include readable permanent tombstones
    max_results (int, optional, default=50): Page size; defaults to 50 and must be between 1 and 1000
    next_token (str, optional): Opaque continuation token
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Returns:
    Page[ServiceIdentityResponse]

```python
service_identities.list(*, owner_principal_id: 'str | None' = None, include_deleted: 'bool | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None, label: 'dict[str, str] | None' = None) -> 'Page[ServiceIdentityResponse]'
```

[service_identities](../service_identities.md) · [Python](../../python.md)
