<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.listEnrollments

List a human user's enrollments

Returns one newest-first page containing pending, expired, consumed, and revoked enrollment metadata. MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user is required. The page never contains raw credentials.

```java
ai.pairsys.goodmem.client.Page<UserEnrollmentResponse> listEnrollments(String userId, java.util.Map<String, Object> query)
```

```java
ai.pairsys.goodmem.client.Page<UserEnrollmentResponse> listEnrollments(ai.pairsys.goodmem.client.models.UserId userId, java.util.Map<String, Object> query)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
ai.pairsys.goodmem.client.Page<UserEnrollmentResponse> listEnrollments(java.util.UUID userId, java.util.Map<String, Object> query)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [UserId](../models/UserId.md)
