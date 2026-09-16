<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.role_assignments.delete

Revoke a scoped role assignment

Soft-revokes one non-ROOT assignment and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS.

Args:
    id (str): Role-assignment UUID

Returns:
    RoleAssignment

```python
access_policy.role_assignments.delete(*, id: 'str') -> 'RoleAssignment'
```

[access_policy.role_assignments](../access_policy.role_assignments.md) · [Python](../../python.md)
