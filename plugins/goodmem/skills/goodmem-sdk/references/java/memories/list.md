<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.list

List memories in a space

Lists all memories within a given space. Pagination is supported via maxResults and nextToken (opaque). nextToken is a URL-safe Base64 string without padding; do not parse or construct it. This is a read-only operation with no side effects and is safe to retry.

AUTHORIZATION: Requires LIST_MEMORY on the exact containing space. Each returned memory must also satisfy READ_MEMORY, either directly or through DIRECT_MEMBERS_OF that space. Both predicates are evaluated in PostgreSQL. Returns NOT_FOUND if the specified space does not exist.

```java
ai.pairsys.goodmem.client.Page<Memory> list(String spaceId)
```

No-filter convenience. Equivalent to passing `null` or a default MemoryListOptions.

```java
ai.pairsys.goodmem.client.Page<Memory> list(String spaceId, MemoryListOptions options)
```

Typed-options overload. See `MemoryListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
ai.pairsys.goodmem.client.Page<Memory> list(ai.pairsys.goodmem.client.models.SpaceId spaceId)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
ai.pairsys.goodmem.client.Page<Memory> list(ai.pairsys.goodmem.client.models.SpaceId spaceId, MemoryListOptions options)
```

Domain-ID typed overload. See `MemoryListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
ai.pairsys.goodmem.client.Page<Memory> list(java.util.UUID spaceId)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
ai.pairsys.goodmem.client.Page<Memory> list(java.util.UUID spaceId, MemoryListOptions options)
```

UUID-typed overload. See `MemoryListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryListOptions](../models/MemoryListOptions.md)
- [SpaceId](../models/SpaceId.md)
