<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.getRaw

Get a memory by ID

Retrieves a single memory by its ID.

AUTHORIZATION: Requires READ_MEMORY on the requested memory; authority may be granted directly or through DIRECT_MEMBERS_OF its containing space. This is a read-only operation with no side effects and is safe to retry. Returns NOT_FOUND if the memory or its parent space does not exist.

Escape hatch. Prefer the typed sibling `get(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
Memory getRaw(String id, java.util.Map<String, Object> query)
```

[memories](../memories.md) · [Java](../../java.md)
