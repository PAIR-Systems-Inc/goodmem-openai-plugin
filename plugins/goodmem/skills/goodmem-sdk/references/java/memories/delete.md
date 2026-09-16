<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.delete

Delete a memory

Permanently deletes a memory and its associated chunks. This operation cannot be undone and immediately removes the memory record from the database.

IDEMPOTENCY: This operation is safe to retry - may return NOT_FOUND if the memory was already deleted or never existed.

AUTHORIZATION: Requires DELETE_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space. Side effects include permanent removal of the memory record and all associated chunk data.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.MemoryId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](../models/MemoryId.md)
