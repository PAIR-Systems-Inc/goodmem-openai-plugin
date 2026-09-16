<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.content

Download memory content

Returns the original binary payload for a memory. The response uses the memory's stored content type when available. Returns 404 when the memory does not have inline content; clients can check original_content_ref from the metadata endpoint to locate external content. Requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Args:
    id (str): The UUID of the memory to download

```python
memories.content(*, id: 'str') -> 'bytes'
```

[memories](../memories.md) · [Python](../../python.md)
