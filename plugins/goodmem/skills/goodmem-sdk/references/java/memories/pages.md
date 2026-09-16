<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.pages

List memory page images

Lists extracted page-image metadata for a memory with optional filters and pagination. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(String id)
```

No-filter convenience. Equivalent to passing `null` or a default MemoryPageListOptions.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(String id, MemoryPageListOptions options)
```

Typed-options overload. See `MemoryPageListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(ai.pairsys.goodmem.client.models.MemoryId id)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(ai.pairsys.goodmem.client.models.MemoryId id, MemoryPageListOptions options)
```

Domain-ID typed overload. See `MemoryPageListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(java.util.UUID id)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pages(java.util.UUID id, MemoryPageListOptions options)
```

UUID-typed overload. See `MemoryPageListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](../models/MemoryId.md)
- [MemoryPageListOptions](../models/MemoryPageListOptions.md)
