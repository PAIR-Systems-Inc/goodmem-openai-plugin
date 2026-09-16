<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.grants.create

Create an authorization grant

Creates one direct grant after resolving its typed policy target and requiring MANAGE_ACCESS. Direct grants cannot confer credential-read or ownership-transfer authority. ALL_AUTHENTICATED grants require an assigned-resource selector. MANAGE_ACCESS and MANAGE_USER_ENROLLMENT require a concrete principal and ANY or EXACT; MANAGE_USER_ENROLLMENT with EXACT must target USER.

Args:
    grant_id (str, optional): Optional caller-provided grant UUID.
    audience (GrantAudience): Audience receiving the grant.
    rule (AccessPolicyRule): Authorization descriptor to grant.

Returns:
    AuthorizationGrant

```python
access_policy.grants.create(*, audience: 'GrantAudience', rule: 'AccessPolicyRule', grant_id: 'str | None' = None) -> 'AuthorizationGrant'
```

[access_policy.grants](../access_policy.grants.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [AccessPolicyRule](../models/AccessPolicyRule.md)
- [GrantAudience](../models/GrantAudience.md)
