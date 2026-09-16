<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.update

Update a human user

Updates only fields present in the request. Empty username or display_name values clear those optional fields. Updating a deleted user fails with 412.

Args:
    id (str): User UUID
    request (UpdateUserRequest | dict): The request payload. Accepts a UpdateUserRequest instance or a plain dict with the same fields.

Returns:
    UserResponse

```python
users.update(*, id: 'str', request: 'UpdateUserRequest | dict') -> 'UserResponse'
```

[users](../users.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateUserRequest](../models/UpdateUserRequest.md)
