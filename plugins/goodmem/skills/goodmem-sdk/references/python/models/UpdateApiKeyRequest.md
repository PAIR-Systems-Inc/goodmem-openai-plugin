<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateApiKeyRequest

Request parameters for updating an API key.

```python
from goodmem.models import UpdateApiKeyRequest
```

- `status` (`Literal['ACTIVE', 'INACTIVE'] | None`, optional): New status for the API key. INACTIVE is permanent; revoked keys cannot be reactivated.
- `replace_labels` (`dict[str, str] | None`, optional): Replace all existing labels with this set. Mutually exclusive with merge_labels. The stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Merge these labels with existing ones. Mutually exclusive with replace_labels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.

[Python](../../python.md)
