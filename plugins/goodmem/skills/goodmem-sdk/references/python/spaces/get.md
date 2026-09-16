<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.get

Get a space by ID

Retrieves a specific space by its unique identifier. Returns the complete space information, including name, labels, embedder configuration, and metadata. Requires READ_SPACE on the requested space. The service distinguishes a missing space from an existing space the caller cannot read. This is a read-only operation safe to retry.

Args:
    id (str): The unique identifier of the space to retrieve

Returns:
    Space

```python
spaces.get(*, id: 'str') -> 'Space'
```

[spaces](../spaces.md) · [Python](../../python.md)
