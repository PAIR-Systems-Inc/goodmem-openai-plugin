<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.revokeEnrollment

Revoke a human-user enrollment

Permanently revokes one outstanding enrollment after requiring MANAGE_USER_ENROLLMENT on its target user. Repeating an authorized revocation succeeds without replacing its original audit provenance. Consumed enrollments cannot be revoked.

```java
void revokeEnrollment(String userId, String enrollmentId)
```

```java
void revokeEnrollment(ai.pairsys.goodmem.client.models.UserId userId, ai.pairsys.goodmem.client.models.EnrollmentId enrollmentId)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void revokeEnrollment(java.util.UUID userId, java.util.UUID enrollmentId)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EnrollmentId](../models/EnrollmentId.md)
- [UserId](../models/UserId.md)
