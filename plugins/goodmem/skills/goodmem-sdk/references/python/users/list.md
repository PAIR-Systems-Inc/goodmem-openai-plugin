<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.list

List human users

Requires LIST_USER on the GoodMem instance and READ_USER on each returned row. Authorization, label filtering, lifecycle filtering, and keyset pagination run in PostgreSQL. include_deleted expands the lifecycle view but grants no access. include_enrollment_summary requests non-secret bootstrap posture only on active rows where MANAGE_USER_ENROLLMENT is independently authorized.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Args:
    include_deleted (bool, optional, default=False): Include readable permanent tombstones
    include_enrollment_summary (bool, optional, default=False): Request non-secret enrollment posture on active rows where the caller also has MANAGE_USER_ENROLLMENT
    max_results (int, optional, default=50): Page size; defaults to 50 and must be between 1 and 1000
    next_token (str, optional): Opaque continuation token
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

Returns:
    Page[UserResponse]

```python
users.list(*, include_deleted: 'bool | None' = None, include_enrollment_summary: 'bool | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None, label: 'dict[str, str] | None' = None) -> 'Page[UserResponse]'
```

[users](../users.md) · [Python](../../python.md)
