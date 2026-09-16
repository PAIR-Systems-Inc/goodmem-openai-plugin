<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.update

Update an embedder

Updates explicitly supplied embedder fields; at least one mutable field is required. Field omission and reset semantics are defined by the request schema, and providerType cannot be changed. Returns 409 if the resulting configuration duplicates another embedder for the owner, and 412 when model-defining fields are changed while the embedder is in use. Requires UPDATE_EMBEDDER on the requested embedder. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

```java
EmbedderResponse update(String id, UpdateEmbedderRequest request)
```

```java
EmbedderResponse update(ai.pairsys.goodmem.client.models.EmbedderId id, UpdateEmbedderRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
EmbedderResponse update(java.util.UUID id, UpdateEmbedderRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[embedders](../embedders.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderId](../models/EmbedderId.md)
- [UpdateEmbedderRequest](../models/UpdateEmbedderRequest.md)
