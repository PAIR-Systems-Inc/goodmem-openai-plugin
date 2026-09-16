<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# embedders.update

Update an embedder

Updates explicitly supplied embedder fields; at least one mutable field is required. Field omission and reset semantics are defined by the request schema, and provider_type cannot be changed. Returns 409 if the resulting configuration duplicates another embedder for the owner, and 412 when model-defining fields are changed while the embedder is in use. Requires UPDATE_EMBEDDER on the requested embedder. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

Args:
    id (str): The unique identifier of the embedder to update
    request (UpdateEmbedderRequest | dict): The request payload. Accepts a UpdateEmbedderRequest instance or a plain dict with the same fields.

Returns:
    EmbedderResponse

```python
embedders.update(*, id: 'str', request: 'UpdateEmbedderRequest | dict') -> 'EmbedderResponse'
```

[embedders](../embedders.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateEmbedderRequest](../models/UpdateEmbedderRequest.md)
