<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.delete

Delete a space

Permanently deletes a space and all associated content. This operation cannot be undone.

CASCADE DELETION: Removes the space record and cascades deletion to associated memories, chunks, and embedder associations. Requires DELETE_SPACE on the requested space. This operation is safe to retry and may return NOT_FOUND if the space was already deleted.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.SpaceId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceId](../models/SpaceId.md)
