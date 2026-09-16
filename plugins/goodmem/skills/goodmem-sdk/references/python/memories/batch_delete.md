<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.batch_delete

Delete memories in batch

Deletes memories using selector entries. Each selector can target either a specific memory ID or a filtered subset scoped to a specific space. Each selected memory requires DELETE_MEMORY; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Args:
    requests (list[BatchDeleteMemorySelectorRequest]): Array of delete selectors

Returns:
    BatchMemoryResponse

```python
memories.batch_delete(*, requests: 'list[BatchDeleteMemorySelectorRequest]') -> 'BatchMemoryResponse'
```

[memories](../memories.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [BatchDeleteMemorySelectorRequest](../models/BatchDeleteMemorySelectorRequest.md)
