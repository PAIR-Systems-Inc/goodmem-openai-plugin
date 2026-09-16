<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# service_identities.get

Get a service identity

Returns a service identity after applying READ_SERVICE_IDENTITY authority. include_deleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority.

Args:
    id (str): Service-identity UUID
    include_deleted (bool, optional, default=False): Permit an authorized read of a permanent tombstone

Returns:
    ServiceIdentityResponse

```python
service_identities.get(*, id: 'str', include_deleted: 'bool | None' = None) -> 'ServiceIdentityResponse'
```

[service_identities](../service_identities.md) · [Python](../../python.md)
