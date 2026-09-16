<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# userEnrollments.complete

Complete human-user enrollment

Exchanges a one-time enrollment credential for the human's initial self-owned API key. This endpoint does not use ordinary API-key authentication. Omit both optional key fields for server generation; a fresh response discloses the raw key exactly once and cannot be safely retried after an ambiguous outcome. Supply and retain both fields for client mode, where only an exact tuple retry is safe and raw material is never echoed. Status precedence is request-shape errors (400), then the same generic authentication failure for every nonblank unusable enrollment (401); key conflicts or concurrent lifecycle winners return 409, rate limits return 429, and unexpected failures return 500.

```java
CompleteUserEnrollmentResponse complete(CompleteUserEnrollmentRequest request)
```

[userEnrollments](../userEnrollments.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [CompleteUserEnrollmentRequest](../models/CompleteUserEnrollmentRequest.md)
