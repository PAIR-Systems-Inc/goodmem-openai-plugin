<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.pagesRaw

List memory page images

Lists extracted page-image metadata for a memory with optional filters and pagination. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Escape hatch. Prefer the typed sibling `pages(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
ai.pairsys.goodmem.client.Page<MemoryPageImage> pagesRaw(String id, java.util.Map<String, Object> query)
```

[memories](../memories.md) · [Java](../../java.md)
