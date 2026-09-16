<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.update

Update a human user

Updates only fields present in the request. Empty username or displayName values clear those optional fields. Updating a deleted user fails with 412.

```java
UserResponse update(String id, UpdateUserRequest request)
```

```java
UserResponse update(ai.pairsys.goodmem.client.models.UserId id, UpdateUserRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
UserResponse update(java.util.UUID id, UpdateUserRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [UpdateUserRequest](../models/UpdateUserRequest.md)
- [UserId](../models/UserId.md)
