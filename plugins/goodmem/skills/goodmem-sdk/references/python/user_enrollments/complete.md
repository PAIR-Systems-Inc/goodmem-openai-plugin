<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# user_enrollments.complete

Complete human-user enrollment

Exchanges a one-time enrollment credential for the human's initial self-owned API key. This endpoint does not use ordinary API-key authentication. Omit both optional key fields for server generation; a fresh response discloses the raw key exactly once and cannot be safely retried after an ambiguous outcome. Supply and retain both fields for client mode, where only an exact tuple retry is safe and raw material is never echoed. Status precedence is request-shape errors (400), then the same generic authentication failure for every nonblank unusable enrollment (401); key conflicts or concurrent lifecycle winners return 409, rate limits return 429, and unexpected failures return 500.

Args:
    enrollment_token (str): Required one-time enrollment credential. Never log or persist it.
    api_key_id (str, optional): Optional client-generated API-key UUID retained for exact retries. Must be supplied together with raw_api_key, or both fields must be omitted.
    raw_api_key (str, optional): Optional canonical client-generated API key. Must be supplied together with api_key_id, never logged, and retained for exact retries; omit both fields for server generation.

Returns:
    CompleteUserEnrollmentResponse

```python
user_enrollments.complete(*, enrollment_token: 'str', api_key_id: 'str | None' = None, raw_api_key: 'str | None' = None) -> 'CompleteUserEnrollmentResponse'
```

[user_enrollments](../user_enrollments.md) · [Python](../../python.md)
