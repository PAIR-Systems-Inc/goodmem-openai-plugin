<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.getRaw

Get an embedder by ID

Retrieves the details of a specific embedder configuration by its unique identifier. Requires READ_EMBEDDER on the requested embedder. The service distinguishes a missing embedder from an existing embedder the caller cannot read. This is a read-only operation with no side effects.

Escape hatch. Prefer the typed sibling `get(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
EmbedderResponse getRaw(String id, java.util.Map<String, Object> query)
```

[embedders](../embedders.md) · [Java](../../java.md)
