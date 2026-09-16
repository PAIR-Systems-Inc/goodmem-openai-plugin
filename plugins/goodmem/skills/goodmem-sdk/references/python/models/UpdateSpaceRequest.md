<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateSpaceRequest

Request parameters for updating a space.

```python
from goodmem.models import UpdateSpaceRequest
```

- `name` (`str | None`, optional): The new name for the space.
- `replace_labels` (`dict[str, str] | None`, optional): Labels to replace all existing labels. Mutually exclusive with merge_labels. JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Labels to merge with existing labels. Mutually exclusive with replace_labels. JSON: `mergeLabels`.

[Python](../../python.md)
