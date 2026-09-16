<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.get_enrollment

Get a human-user enrollment

Returns non-secret metadata for one current or historical enrollment. The target user is resolved before the enrollment, and MANAGE_USER_ENROLLMENT with ANY or EXACT authority on that user is required. Raw enrollment tokens are never returned.

Args:
    user_id (str): Human-user UUID
    enrollment_id (str): Enrollment UUID

Returns:
    UserEnrollmentResponse

```python
users.get_enrollment(*, user_id: 'str', enrollment_id: 'str') -> 'UserEnrollmentResponse'
```

[users](../users.md) · [Python](../../python.md)
