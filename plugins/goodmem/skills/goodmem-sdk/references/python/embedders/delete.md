<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# embedders.delete

Delete an embedder

Permanently deletes an embedder configuration. This operation cannot be undone and removes the embedder record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete embeddings previously created with this embedder - existing embeddings remain accessible.

CONFLICT: Returns HTTP 409 Conflict if the embedder is still referenced by a space. Requires DELETE_EMBEDDER on the requested embedder.

Args:
    id (str): The unique identifier of the embedder to delete

```python
embedders.delete(*, id: 'str') -> 'None'
```

[embedders](../embedders.md) · [Python](../../python.md)
