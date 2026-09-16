<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.pages_image

Download memory page image content

Downloads inline bytes for one page image. The page index is required. The optional dpi and content type query parameters act as rendition filters; if omitted, the server returns the unique rendition for that page or rejects ambiguous matches. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Args:
    id (str): Memory UUID
    page_index (int): 0-based page index
    dpi (int, optional): Optional rendition filter. If omitted, the unique page-image rendition for the page is returned; if multiple renditions exist, specify dpi and/or content_type.
    content_type (str, optional): Optional rendition filter. MIME type of the desired page image, such as image/png.

```python
memories.pages_image(*, id: 'str', page_index: 'int', dpi: 'int | None' = None, content_type: 'str | None' = None) -> 'bytes'
```

[memories](../memories.md) · [Python](../../python.md)
