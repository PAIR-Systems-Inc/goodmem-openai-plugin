<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.retrieve_memory_log_policies.list

List RetrieveMemory log policies

Lists RetrieveMemory log policies with optional tombstone, active-time, name, label, sort, and pagination filters.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Args:
    include_deleted (bool, optional, default=False): Whether to include tombstoned policies. Also accepts include_deleted.
    name_filter (str, optional): Case-insensitive substring filter on policy display names. Also accepts name_filter.
    active_at (int, optional): Only return policies active at this millisecond epoch timestamp. Also accepts active_at.
    max_results (int, optional, default=50): Maximum number of policies to return. Also accepts max_results.
    next_token (str, optional): Opaque pagination token returned by the previous list response. Also accepts next_token.
    sort_by (Literal['created_at', 'updated_at', 'display_name'], optional, default='created_at'): Sort field: created_at, updated_at, or display_name. Also accepts sort_by.
    sort_order (SortOrder, optional, default='DESCENDING'): Sort order. Also accepts sort_order.
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Returns:
    Page[RetrieveMemoryLogPolicy]

```python
admin.retrieve_memory_log_policies.list(*, include_deleted: 'bool | None' = None, name_filter: 'str | None' = None, active_at: 'int | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None, sort_by: "Literal['created_at', 'updated_at', 'display_name'] | None" = None, sort_order: 'SortOrder | None' = None, label: 'dict[str, str] | None' = None) -> 'Page[RetrieveMemoryLogPolicy]'
```

[admin.retrieve_memory_log_policies](../admin.retrieve_memory_log_policies.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [SortOrder](../models/SortOrder.md)
