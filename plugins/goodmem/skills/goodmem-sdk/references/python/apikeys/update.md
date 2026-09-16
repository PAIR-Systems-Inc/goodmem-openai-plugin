<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# apikeys.update

Update an API key

Updates an existing API key's labels or lifecycle status. Key ID, subject, ownership, key material, validity window, and creation audit fields remain immutable. Label changes require UPDATE_API_KEY; setting status=INACTIVE permanently revokes the key and requires DELETE_API_KEY; a request doing both requires both operations. Revoked keys cannot be reactivated. Side effects include updating administrative audit fields and, for revocation, recording the revocation time and actor.

Args:
    id (str): The UUID of the API key to update
    request (UpdateApiKeyRequest | dict): The request payload. Accepts a UpdateApiKeyRequest instance or a plain dict with the same fields.

Returns:
    ApiKeyResponse

```python
apikeys.update(*, id: 'str', request: 'UpdateApiKeyRequest | dict') -> 'ApiKeyResponse'
```

[apikeys](../apikeys.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateApiKeyRequest](../models/UpdateApiKeyRequest.md)
