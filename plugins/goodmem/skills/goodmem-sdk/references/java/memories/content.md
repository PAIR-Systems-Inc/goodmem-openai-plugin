<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.content

Download memory content

Returns the original binary payload for a memory. The response uses the memory's stored content type when available. Returns 404 when the memory does not have inline content; clients can check originalContentRef from the metadata endpoint to locate external content. Requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```java
byte[] content(String id)
```

```java
byte[] content(ai.pairsys.goodmem.client.models.MemoryId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
byte[] content(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](../models/MemoryId.md)
