<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.create

Create a human user

Creates one dormant human user after requiring instance-wide CREATE_USER authority. Creation does not issue a credential or create a role, grant, or authentication mapping.

```java
UserResponse create(CreateUserRequest request)
```

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [CreateUserRequest](../models/CreateUserRequest.md)
