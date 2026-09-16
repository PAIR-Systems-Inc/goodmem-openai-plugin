<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# admin.retrieveMemoryLogPoliciesDelete

Delete a RetrieveMemory log policy

Idempotently tombstones an immutable RetrieveMemory log policy.

```java
RetrieveMemoryLogPolicy retrieveMemoryLogPoliciesDelete(String id, DeleteRetrieveMemoryLogPolicyRequest request)
```

```java
RetrieveMemoryLogPolicy retrieveMemoryLogPoliciesDelete(java.util.UUID id, DeleteRetrieveMemoryLogPolicyRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[admin](../admin.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [DeleteRetrieveMemoryLogPolicyRequest](../models/DeleteRetrieveMemoryLogPolicyRequest.md)
