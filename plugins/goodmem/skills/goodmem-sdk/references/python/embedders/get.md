<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# embedders.get

Get an embedder by ID

Retrieves the details of a specific embedder configuration by its unique identifier. Requires READ_EMBEDDER on the requested embedder. The service distinguishes a missing embedder from an existing embedder the caller cannot read. This is a read-only operation with no side effects.

Args:
    id (str): The unique identifier of the embedder to retrieve
    include_credentials (bool, optional, default=False): Whether to return stored credentials. Also accepts include_credentials. Requires READ_EMBEDDER_CREDENTIALS in addition to READ_EMBEDDER.

Returns:
    EmbedderResponse

```python
embedders.get(*, id: 'str', include_credentials: 'bool | None' = None) -> 'EmbedderResponse'
```

[embedders](../embedders.md) · [Python](../../python.md)
