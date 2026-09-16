<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.get

Get an embedder by ID

Retrieves the details of a specific embedder configuration by its unique identifier. Requires READ_EMBEDDER on the requested embedder. The service distinguishes a missing embedder from an existing embedder the caller cannot read. This is a read-only operation with no side effects.

```java
EmbedderResponse get(String id)
```

No-filter convenience. Equivalent to passing `null` or a default EmbedderGetOptions.

```java
EmbedderResponse get(String id, EmbedderGetOptions options)
```

Typed-options overload. See `EmbedderGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
EmbedderResponse get(ai.pairsys.goodmem.client.models.EmbedderId id)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
EmbedderResponse get(ai.pairsys.goodmem.client.models.EmbedderId id, EmbedderGetOptions options)
```

Domain-ID typed overload. See `EmbedderGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
EmbedderResponse get(java.util.UUID id)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
EmbedderResponse get(java.util.UUID id, EmbedderGetOptions options)
```

UUID-typed overload. See `EmbedderGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[embedders](../embedders.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderGetOptions](../models/EmbedderGetOptions.md)
- [EmbedderId](../models/EmbedderId.md)
