<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.revoke_enrollment

Revoke a human-user enrollment

Permanently revokes one outstanding enrollment after requiring MANAGE_USER_ENROLLMENT on its target user. Repeating an authorized revocation succeeds without replacing its original audit provenance. Consumed enrollments cannot be revoked.

Args:
    user_id (str): Human-user UUID
    enrollment_id (str): Enrollment UUID

```python
users.revoke_enrollment(*, user_id: 'str', enrollment_id: 'str') -> 'None'
```

[users](../users.md) · [Python](../../python.md)
