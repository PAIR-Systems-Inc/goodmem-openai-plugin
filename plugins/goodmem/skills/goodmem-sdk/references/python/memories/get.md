<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.get

Get a memory by ID

Retrieves a single memory by its ID.

AUTHORIZATION: Requires READ_MEMORY on the requested memory; authority may be granted directly or through DIRECT_MEMBERS_OF its containing space. This is a read-only operation with no side effects and is safe to retry. Returns NOT_FOUND if the memory or its parent space does not exist.

Args:
    id (str): The UUID of the memory to retrieve
    include_content (bool, optional, server default=False): Whether to include the original content in the response (defaults to false).
    include_processing_history (bool, optional, server default=False): Whether to include background job processing history in the response (defaults to false).

Returns:
    Memory

```python
memories.get(*, id: 'str', include_content: 'bool | None' = None, include_processing_history: 'bool | None' = None) -> 'Memory'
```

[memories](../memories.md) · [Python](../../python.md)
