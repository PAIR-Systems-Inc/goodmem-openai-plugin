<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.grantsCreate

Create an authorization grant

Creates one direct grant after resolving its typed policy target and requiring MANAGE_ACCESS. Direct grants cannot confer credential-read or ownership-transfer authority. ALL_AUTHENTICATED grants require an assigned-resource selector. MANAGE_ACCESS and MANAGE_USER_ENROLLMENT require a concrete principal and ANY or EXACT; MANAGE_USER_ENROLLMENT with EXACT must target USER.

```java
AuthorizationGrant grantsCreate(CreateAuthorizationGrantRequest request)
```

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [CreateAuthorizationGrantRequest](../models/CreateAuthorizationGrantRequest.md)
