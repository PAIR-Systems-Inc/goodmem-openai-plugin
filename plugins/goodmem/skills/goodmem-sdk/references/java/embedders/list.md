<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.list

List embedders

Retrieves a list of embedder configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_EMBEDDER on the GoodMem instance. Each returned embedder must also be visible through READ_EMBEDDER; unauthorized embedders are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

```java
java.util.List<EmbedderResponse> list()
```

No-filter convenience. Equivalent to passing `null` or a default EmbedderListOptions.

```java
java.util.List<EmbedderResponse> list(EmbedderListOptions options)
```

Typed-options overload. See `EmbedderListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[embedders](../embedders.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderListOptions](../models/EmbedderListOptions.md)
