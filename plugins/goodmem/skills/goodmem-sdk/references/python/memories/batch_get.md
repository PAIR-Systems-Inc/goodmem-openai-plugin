<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.batch_get

Get multiple memories by ID

Retrieves multiple memories in a single operation, with individual success/failure results. Each item requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Args:
    memory_ids (list[str]): Array of memory IDs to retrieve
    include_content (bool, optional, default=False): Whether to include the original content in the response
    include_processing_history (bool, optional, default=False): Whether to include background job processing history for each memory

Returns:
    BatchMemoryResponse

```python
memories.batch_get(*, memory_ids: 'list[str]', include_content: 'bool | None' = None, include_processing_history: 'bool | None' = None) -> 'BatchMemoryResponse'
```

[memories](../memories.md) · [Python](../../python.md)
