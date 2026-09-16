<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.get

Get a user by ID or email

Retrieves a user by ID or email address. Exactly one of `id` and `email` must be provided. For getting your own profile, use `client.users.me()`.

Args:
    email (str, optional): The user's email address. Mutually exclusive with `id` — exactly one must be provided.
    id (str, optional): The user's UUID. Mutually exclusive with `email` — exactly one must be provided.
    include_deleted (bool, optional, server default=False): Permit an authorized read of a permanent tombstone

Returns:
    UserResponse

```python
users.get(*, email: 'str | None' = None, id: 'str | None' = None, include_deleted: 'bool | None' = None) -> 'UserResponse'
```

[users](../users.md) · [Python](../../python.md)
