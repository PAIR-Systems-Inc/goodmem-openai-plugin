<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.delete

Delete a space

Permanently deletes a space and all associated content. This operation cannot be undone.

CASCADE DELETION: Removes the space record and cascades deletion to associated memories, chunks, and embedder associations. Requires DELETE_SPACE on the requested space. This operation is safe to retry and may return NOT_FOUND if the space was already deleted.

Args:
    id (str): The unique identifier of the space to delete

```python
spaces.delete(*, id: 'str') -> 'None'
```

[spaces](../spaces.md) · [Python](../../python.md)
