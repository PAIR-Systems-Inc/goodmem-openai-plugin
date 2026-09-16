<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.delete

Delete a reranker

Permanently deletes a reranker configuration. This operation cannot be undone and immediately removes the reranker record from the database.

SIDE EFFECTS: Invalidates any cached references to this reranker; does not affect historical usage data or audit logs. Requires DELETE_RERANKER on the requested reranker. This operation is safe to retry - may return NOT_FOUND if already deleted.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.RerankerId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[rerankers](../rerankers.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RerankerId](../models/RerankerId.md)
