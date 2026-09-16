<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.list

List memories in a space

Lists memories within a given space. Results are paginated — the returned `Page` eagerly fetches the first page. Access `.data` for items and `.next_token` to resume. Use `for mem in page` to auto-paginate all pages, `page_size` to control items per API call, and `max_items` to cap total results.

Args:
    space_id (str): The UUID of the space containing the memories
    filter (str, optional): Metadata filter expression for list results. See [Metadata Filters Guide](https://docs.goodmem.ai/docs/how-to/metadata-filters) and [Filter Expressions Reference](https://docs.goodmem.ai/docs/reference/filter-expressions) for usage.
    include_content (bool, optional, server default=False): Whether to include the original content in the response (defaults to false).
    include_processing_history (bool, optional, server default=False): Whether to include background job processing history in the response (defaults to false).
    sort_by (Literal['created_at', 'updated_at', 'content_type', 'processing_status'], optional): Field to sort by (e.g., 'created_at').
    sort_order (SortOrder, optional): Sort direction (ASCENDING or DESCENDING).
    status_filter (Literal['PENDING', 'PROCESSING', 'COMPLETED', 'FAILED'], optional): Filter memories by processing status (PENDING, PROCESSING, COMPLETED, FAILED).
    page_size (int, optional): Number of results per page (defaults to 50, clamped to [1, 500] by the server). A smaller value will reduce the latency of each page — so you get items faster each page, but increase the number of requests made to the server. Use `max_items` to cap total results.
    max_items (int, optional): Maximum total number of items to return across all pages. When set, iteration stops after this many items. If left unset, all pages will be fetched.
    next_token (str, optional): Opaque pagination token for the next page.

Returns:
    Page[Memory]

```python
memories.list(*, space_id: 'str', filter: 'str | None' = None, include_content: 'bool | None' = None, include_processing_history: 'bool | None' = None, sort_by: "Literal['created_at', 'updated_at', 'content_type', 'processing_status'] | None" = None, sort_order: 'SortOrder | None' = None, status_filter: "Literal['PENDING', 'PROCESSING', 'COMPLETED', 'FAILED'] | None" = None, page_size: 'int | None' = None, max_items: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[Memory]'
```

[memories](../memories.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [SortOrder](../models/SortOrder.md)
