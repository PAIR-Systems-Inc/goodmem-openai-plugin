<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.grants.delete

Revoke an authorization grant

Soft-revokes one grant and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS on the target.

Args:
    id (str): Grant UUID

Returns:
    AuthorizationGrant

```python
access_policy.grants.delete(*, id: 'str') -> 'AuthorizationGrant'
```

[access_policy.grants](../access_policy.grants.md) · [Python](../../python.md)
