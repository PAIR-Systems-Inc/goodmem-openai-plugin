<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.getEnrollment

Get a human-user enrollment

Returns non-secret metadata for one current or historical enrollment. The target user is resolved before the enrollment, and MANAGE_USER_ENROLLMENT with ANY or EXACT authority on that user is required. Raw enrollment tokens are never returned.

```java
UserEnrollmentResponse getEnrollment(String userId, String enrollmentId)
```

```java
UserEnrollmentResponse getEnrollment(ai.pairsys.goodmem.client.models.UserId userId, ai.pairsys.goodmem.client.models.EnrollmentId enrollmentId)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
UserEnrollmentResponse getEnrollment(java.util.UUID userId, java.util.UUID enrollmentId)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EnrollmentId](../models/EnrollmentId.md)
- [UserId](../models/UserId.md)
