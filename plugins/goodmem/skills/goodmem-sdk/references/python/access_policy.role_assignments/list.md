<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.role_assignments.list

List scoped role assignments

Lists assignments attached to one required INSTANCE or SPACE boundary after requiring MANAGE_ACCESS. Continuation tokens are bound to the caller and filters.

Args:
    resource_kind (Literal['INSTANCE', 'SPACE']): Required INSTANCE or SPACE kind
    resource_id (str, optional): Required space UUID; omitted for INSTANCE
    include_revoked (bool, optional, default=False): Include revoked history
    max_results (int, optional, default=50): Page size; 0 or omission uses the default of 50, maximum 1,000
    next_token (str, optional): Opaque continuation token

Returns:
    Page[RoleAssignment]

```python
access_policy.role_assignments.list(*, resource_kind: "Literal['INSTANCE', 'SPACE']", resource_id: 'str | None' = None, include_revoked: 'bool | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[RoleAssignment]'
```

[access_policy.role_assignments](../access_policy.role_assignments.md) · [Python](../../python.md)
