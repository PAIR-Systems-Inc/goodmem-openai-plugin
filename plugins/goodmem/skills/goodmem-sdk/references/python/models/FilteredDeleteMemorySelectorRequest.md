<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# FilteredDeleteMemorySelectorRequest

Filtered selector scoped to a specific space

```python
from goodmem.models import FilteredDeleteMemorySelectorRequest
```

- `space_id` (`str`, required): Space ID scope for the filtered delete JSON: `spaceId`.
- `status_filter` (`Literal['PENDING', 'PROCESSING', 'COMPLETED', 'FAILED'] | None`, optional): Optional processing status filter (PENDING, PROCESSING, COMPLETED, FAILED) JSON: `statusFilter`.
- `filter` (`str | None`, optional): Optional metadata filter expression

[Python](../../python.md)
