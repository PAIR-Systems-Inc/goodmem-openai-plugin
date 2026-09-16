<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.delete

Delete a human user

Permanently soft-deletes the user and invalidates credentials acting for that subject. The GoodMem instance owner cannot be deleted; transfer ownership first. Repeating an authorized delete succeeds without rewriting audit data.

Args:
    id (str): User UUID

```python
users.delete(*, id: 'str') -> 'None'
```

[users](../users.md) · [Python](../../python.md)
