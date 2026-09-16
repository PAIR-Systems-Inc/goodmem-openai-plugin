<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.get

Get a memory by ID

Retrieves a single memory by its ID.

AUTHORIZATION: Requires READ_MEMORY on the requested memory; authority may be granted directly or through DIRECT_MEMBERS_OF its containing space. This is a read-only operation with no side effects and is safe to retry. Returns NOT_FOUND if the memory or its parent space does not exist.

```java
Memory get(String id)
```

No-filter convenience. Equivalent to passing `null` or a default MemoryGetOptions.

```java
Memory get(String id, MemoryGetOptions options)
```

Typed-options overload. See `MemoryGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
Memory get(ai.pairsys.goodmem.client.models.MemoryId id)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
Memory get(ai.pairsys.goodmem.client.models.MemoryId id, MemoryGetOptions options)
```

Domain-ID typed overload. See `MemoryGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
Memory get(java.util.UUID id)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
Memory get(java.util.UUID id, MemoryGetOptions options)
```

UUID-typed overload. See `MemoryGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryGetOptions](../models/MemoryGetOptions.md)
- [MemoryId](../models/MemoryId.md)
