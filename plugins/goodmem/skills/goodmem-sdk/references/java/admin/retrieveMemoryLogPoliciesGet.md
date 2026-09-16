<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# admin.retrieveMemoryLogPoliciesGet

Get a RetrieveMemory log policy

Retrieves a live RetrieveMemory log policy by UUID, or a tombstoned policy when includeDeleted is true.

```java
RetrieveMemoryLogPolicy retrieveMemoryLogPoliciesGet(String id, java.util.Map<String, Object> query)
```

```java
RetrieveMemoryLogPolicy retrieveMemoryLogPoliciesGet(java.util.UUID id, java.util.Map<String, Object> query)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[admin](../admin.md) · [Java](../../java.md)
