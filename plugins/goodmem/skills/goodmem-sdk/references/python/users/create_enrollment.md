<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# users.create_enrollment

Create a human-user enrollment

Creates a short-lived, one-time enrollment credential for an existing dormant human. Requires MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user. The raw credential is returned only once. rotate_existing atomically revokes and replaces a live enrollment; an expired enrollment is replaced automatically.

Args:
    user_id (str): Human-user UUID
    request (CreateUserEnrollmentRequest | dict | None, optional): Optional payload. Accepts a CreateUserEnrollmentRequest instance, a plain dict with the same fields, or ``None`` to send no body. Only specified fields are sent to the server.

Returns:
    CreateUserEnrollmentResponse

```python
users.create_enrollment(*, user_id: 'str', request: 'CreateUserEnrollmentRequest | dict | None' = None) -> 'CreateUserEnrollmentResponse'
```

[users](../users.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [CreateUserEnrollmentRequest](../models/CreateUserEnrollmentRequest.md)
