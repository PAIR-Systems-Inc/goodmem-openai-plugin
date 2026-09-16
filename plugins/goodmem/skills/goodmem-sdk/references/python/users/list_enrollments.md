<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.list_enrollments

List a human user's enrollments

Returns one newest-first page containing pending, expired, consumed, and revoked enrollment metadata. MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user is required. The page never contains raw credentials.

Args:
    user_id (str): Human-user UUID
    max_results (int, optional, default=50): Page size; defaults to 50 and must be between 1 and 1000
    next_token (str, optional): Opaque continuation token

Returns:
    Page[UserEnrollmentResponse]

```python
users.list_enrollments(*, user_id: 'str', max_results: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[UserEnrollmentResponse]'
```

[users](../users.md) · [Python](../../python.md)
