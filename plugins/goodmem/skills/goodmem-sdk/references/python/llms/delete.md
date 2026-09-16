<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# llms.delete

Delete an LLM

Permanently deletes an LLM configuration. This operation cannot be undone and removes the LLM record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete any previously generated content using this LLM - existing generations remain accessible. Requires DELETE_LLM on the requested LLM.

Args:
    id (str): The unique identifier of the LLM to delete

```python
llms.delete(*, id: 'str') -> 'None'
```

[llms](../llms.md) · [Python](../../python.md)
