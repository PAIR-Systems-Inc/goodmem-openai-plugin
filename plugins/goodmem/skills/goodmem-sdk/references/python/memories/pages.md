<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.pages

List memory page images

Lists extracted page-image metadata for a memory with optional filters and pagination. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Args:
    id (str): Memory UUID
    start_page_index (int, optional): Optional lower bound for returned page indices, inclusive.
    end_page_index (int, optional): Optional upper bound for returned page indices, inclusive.
    dpi (int, optional): Optional rendition filter for page-image DPI.
    content_type (str, optional): Optional rendition filter for page-image MIME type, such as image/png.
    max_results (int, optional): Maximum number of results per page.
    next_token (str, optional): Opaque pagination token for the next page. Do not parse or construct it.

Returns:
    Page[MemoryPageImage]

```python
memories.pages(*, id: 'str', start_page_index: 'int | None' = None, end_page_index: 'int | None' = None, dpi: 'int | None' = None, content_type: 'str | None' = None, max_results: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[MemoryPageImage]'
```

[memories](../memories.md) · [Python](../../python.md)
