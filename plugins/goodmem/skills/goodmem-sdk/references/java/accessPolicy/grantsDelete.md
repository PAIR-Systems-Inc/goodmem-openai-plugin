<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.grantsDelete

Revoke an authorization grant

Soft-revokes one grant and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS on the target.

```java
AuthorizationGrant grantsDelete(String id)
```

```java
AuthorizationGrant grantsDelete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)
