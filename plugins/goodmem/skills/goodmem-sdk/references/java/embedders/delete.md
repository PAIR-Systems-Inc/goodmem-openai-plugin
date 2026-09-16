<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.delete

Delete an embedder

Permanently deletes an embedder configuration. This operation cannot be undone and removes the embedder record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete embeddings previously created with this embedder - existing embeddings remain accessible.

CONFLICT: Returns HTTP 409 Conflict if the embedder is still referenced by a space. Requires DELETE_EMBEDDER on the requested embedder.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.EmbedderId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[embedders](../embedders.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderId](../models/EmbedderId.md)
