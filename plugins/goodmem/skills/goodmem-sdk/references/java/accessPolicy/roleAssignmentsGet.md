<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.roleAssignmentsGet

Get a scoped role assignment

Reads one live assignment, or one revoked historical assignment when includeRevoked is true, after requiring MANAGE_ACCESS on its policy target.

```java
RoleAssignment roleAssignmentsGet(String id, java.util.Map<String, Object> query)
```

```java
RoleAssignment roleAssignmentsGet(java.util.UUID id, java.util.Map<String, Object> query)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)
