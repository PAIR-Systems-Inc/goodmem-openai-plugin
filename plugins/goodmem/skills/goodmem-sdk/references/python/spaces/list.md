<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.list

List spaces

List spaces accessible to the caller, with optional filtering by owner, labels, and name. Results are paginated — the returned `Page` eagerly fetches the first page. Access `.data` for items and `.next_token` to resume. Use `for space in page` to auto-paginate all pages, `page_size` to control items per API call, and `max_items` to cap total results.

Args:
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).
    name_filter (str, optional): Filter spaces by name using glob pattern matching.
    owner_id (str, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-space READ_SPACE filtering.
    sort_by (Literal['created_time', 'updated_time', 'name'], optional, server default='created_time'): Field to sort by: `'created_time'`, `'updated_time'`, or `'name'` (default: `'created_time'`). Unsupported values return INVALID_ARGUMENT.
    sort_order (SortOrder, optional, server default='DESCENDING'): Sort order (`ASCENDING` or `DESCENDING`, default: `DESCENDING`).
    page_size (int, optional): Number of results per page (defaults to 50, clamped to [1, 1000] by the server).
    max_items (int, optional): Maximum total number of items to return across all pages.
    next_token (str, optional): Opaque pagination token for the next page.

Returns:
    Page[Space]

```python
spaces.list(*, label: 'dict[str, str] | None' = None, name_filter: 'str | None' = None, owner_id: 'str | None' = None, sort_by: "Literal['created_time', 'updated_time', 'name'] | None" = None, sort_order: 'SortOrder | None' = None, page_size: 'int | None' = None, max_items: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[Space]'
```

[spaces](../spaces.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [SortOrder](../models/SortOrder.md)
