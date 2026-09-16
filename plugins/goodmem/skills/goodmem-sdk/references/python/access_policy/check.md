<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.check

Check effective authorization

Evaluates 1 to 50 concrete operation-and-target checks under the authenticated caller's live authority and any API-key ceiling. Results are positional and advisory: missing targets and denied operations both return allowed=false, and every later resource request performs fresh authorization. Top-level creates and LIST_API_KEY target INSTANCE; CREATE_MEMORY and LIST_MEMORY target their parent SPACE; reads, mutations, proxy operations, and access-policy administration target concrete resources. LIST_RETRIEVE_MEMORY_LOG_POLICY is rejected because its current candidate-based list rule has no instance-wide preflight.

Args:
    checks (list[AuthorizationCheck]): Concrete checks evaluated in request order.

Returns:
    CheckAuthorizationsResponse

```python
access_policy.check(*, checks: 'list[AuthorizationCheck]') -> 'CheckAuthorizationsResponse'
```

[access_policy](../access_policy.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [AuthorizationCheck](../models/AuthorizationCheck.md)
