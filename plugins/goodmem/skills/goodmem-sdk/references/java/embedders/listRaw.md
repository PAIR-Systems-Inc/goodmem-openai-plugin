<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.listRaw

List embedders

Retrieves a list of embedder configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_EMBEDDER on the GoodMem instance. Each returned embedder must also be visible through READ_EMBEDDER; unauthorized embedders are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
java.util.List<EmbedderResponse> listRaw(java.util.Map<String, Object> query)
```

[embedders](../embedders.md) · [Java](../../java.md)
