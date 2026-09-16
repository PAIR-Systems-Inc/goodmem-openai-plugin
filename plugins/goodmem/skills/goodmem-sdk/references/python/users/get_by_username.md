<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.get_by_username

Get user by username

Returns a user selected by exact username after applying READ_USER authority. include_deleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority. Missing and unauthorized matches both return 404 so this guessable identifier cannot reveal whether a user exists.

Args:
    username (str): Exact username
    include_deleted (bool, optional, default=False): Permit an authorized read of a permanent tombstone

Returns:
    UserResponse

```python
users.get_by_username(*, username: 'str', include_deleted: 'bool | None' = None) -> 'UserResponse'
```

[users](../users.md) · [Python](../../python.md)
