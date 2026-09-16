<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# service_identities.delete

Delete a service identity

Permanently soft-deletes the principal. Its stored credentials remain audit records but can no longer authenticate because their subject is deleted. Repeating an authorized delete succeeds without rewriting audit data.

Args:
    id (str): Service-identity UUID

```python
service_identities.delete(*, id: 'str') -> 'None'
```

[service_identities](../service_identities.md) · [Python](../../python.md)
