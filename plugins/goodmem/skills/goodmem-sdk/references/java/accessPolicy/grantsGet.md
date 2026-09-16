<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.grantsGet

Get an authorization grant

Reads one live grant, or one revoked historical grant when includeRevoked is true, after requiring MANAGE_ACCESS on its policy target.

```java
AuthorizationGrant grantsGet(String id, java.util.Map<String, Object> query)
```

```java
AuthorizationGrant grantsGet(java.util.UUID id, java.util.Map<String, Object> query)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)
