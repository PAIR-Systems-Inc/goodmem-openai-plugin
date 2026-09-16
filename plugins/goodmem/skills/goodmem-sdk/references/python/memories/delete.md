<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.delete

Delete a memory

Permanently deletes a memory and its associated chunks. This operation cannot be undone and immediately removes the memory record from the database.

IDEMPOTENCY: This operation is safe to retry - may return NOT_FOUND if the memory was already deleted or never existed.

AUTHORIZATION: Requires DELETE_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space. Side effects include permanent removal of the memory record and all associated chunk data.

Args:
    id (str): The UUID of the memory to delete

```python
memories.delete(*, id: 'str') -> 'None'
```

[memories](../memories.md) · [Python](../../python.md)
