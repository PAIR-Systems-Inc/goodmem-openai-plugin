<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.createEnrollment

Create a human-user enrollment

Creates a short-lived, one-time enrollment credential for an existing dormant human. Requires MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user. The raw credential is returned only once. rotateExisting atomically revokes and replaces a live enrollment; an expired enrollment is replaced automatically.

```java
CreateUserEnrollmentResponse createEnrollment(String userId, CreateUserEnrollmentRequest request)
```

```java
CreateUserEnrollmentResponse createEnrollment(ai.pairsys.goodmem.client.models.UserId userId, CreateUserEnrollmentRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
CreateUserEnrollmentResponse createEnrollment(java.util.UUID userId, CreateUserEnrollmentRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [CreateUserEnrollmentRequest](../models/CreateUserEnrollmentRequest.md)
- [UserId](../models/UserId.md)
