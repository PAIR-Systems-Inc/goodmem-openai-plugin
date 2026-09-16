<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.roleAssignmentsDelete

Revoke a scoped role assignment

Soft-revokes one non-ROOT assignment and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS.

```java
RoleAssignment roleAssignmentsDelete(String id)
```

```java
RoleAssignment roleAssignmentsDelete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)
