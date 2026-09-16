<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.grants.get

Get an authorization grant

Reads one live grant, or one revoked historical grant when include_revoked is true, after requiring MANAGE_ACCESS on its policy target.

Args:
    id (str): Grant UUID
    include_revoked (bool, optional, default=False): Include a revoked historical row

Returns:
    AuthorizationGrant

```python
access_policy.grants.get(*, id: 'str', include_revoked: 'bool | None' = None) -> 'AuthorizationGrant'
```

[access_policy.grants](../access_policy.grants.md) · [Python](../../python.md)
