<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# apikeys.get

Get an API key

Returns complete non-secret metadata for one existing credential after requiring effective READ_API_KEY authority. The immutable ceiling is always complete and ceiling_omitted is false. Raw key material and hashes are never returned.

Args:
    id (str): API-key UUID

Returns:
    ApiKeyResponse

```python
apikeys.get(*, id: 'str') -> 'ApiKeyResponse'
```

[apikeys](../apikeys.md) · [Python](../../python.md)
