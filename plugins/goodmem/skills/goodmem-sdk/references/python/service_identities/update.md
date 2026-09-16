<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# service_identities.update

Update a service identity

Updates only fields present in the request. Empty description clears that optional field. Ownership changes use the dedicated transfer endpoint.

Args:
    id (str): Service-identity UUID
    request (UpdateServiceIdentityRequest | dict): The request payload. Accepts a UpdateServiceIdentityRequest instance or a plain dict with the same fields.

Returns:
    ServiceIdentityResponse

```python
service_identities.update(*, id: 'str', request: 'UpdateServiceIdentityRequest | dict') -> 'ServiceIdentityResponse'
```

[service_identities](../service_identities.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateServiceIdentityRequest](../models/UpdateServiceIdentityRequest.md)
