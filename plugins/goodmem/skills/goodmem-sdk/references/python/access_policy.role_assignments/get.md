<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.role_assignments.get

Get a scoped role assignment

Reads one live assignment, or one revoked historical assignment when include_revoked is true, after requiring MANAGE_ACCESS on its policy target.

Args:
    id (str): Role-assignment UUID
    include_revoked (bool, optional, default=False): Include a revoked historical row

Returns:
    RoleAssignment

```python
access_policy.role_assignments.get(*, id: 'str', include_revoked: 'bool | None' = None) -> 'RoleAssignment'
```

[access_policy.role_assignments](../access_policy.role_assignments.md) · [Python](../../python.md)
