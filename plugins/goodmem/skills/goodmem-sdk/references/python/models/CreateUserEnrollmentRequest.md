<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# CreateUserEnrollmentRequest

Options for issuing a one-time enrollment credential to the user named by the request path.

- `enrollment_id` (`str | None`, optional): Optional client-provided enrollment UUID; generated when omitted. JSON: `enrollmentId`.
- `rotate_existing` (`bool | None`, optional): Whether an existing live enrollment may be revoked and atomically replaced. JSON: `rotateExisting`.

[Python](../../python.md)
