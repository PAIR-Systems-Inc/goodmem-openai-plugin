<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# apikeys.delete

Delete an API key

Delete an API key

Permanently revokes an API key and immediately rejects it for future authentication. The durable credential and audit history remain stored. This operation requires DELETE_API_KEY and records the revocation time and actor; it cannot be undone. PUT /v1/apikeys/{id} with status=INACTIVE performs the same permanent revocation.

Args:
    id (str): The UUID of the API key to delete

Returns:
    None

```python
apikeys.delete(*, id: 'str') -> 'None'
```

[apikeys](../apikeys.md) · [Python](../../python.md)
