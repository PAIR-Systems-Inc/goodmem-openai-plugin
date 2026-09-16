<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# rerankers.delete

Delete a reranker

Permanently deletes a reranker configuration. This operation cannot be undone and immediately removes the reranker record from the database.

SIDE EFFECTS: Invalidates any cached references to this reranker; does not affect historical usage data or audit logs. Requires DELETE_RERANKER on the requested reranker. This operation is safe to retry - may return NOT_FOUND if already deleted.

Args:
    id (str): The unique identifier of the reranker to delete

```python
rerankers.delete(*, id: 'str') -> 'None'
```

[rerankers](../rerankers.md) · [Python](../../python.md)
