<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.transferOwnership

Transfer ownership of a space

Transfers an existing space to another active human or service principal. The current space owner, the GoodMem instance owner, or an instance administrator may transfer it; a space-scoped administrator cannot. Only owner and update-audit fields change. Memories, embedder associations, grants, and role assignments remain unchanged. This operation is not idempotent under response semantics: after an unknown outcome, read the space before retrying.

```java
TransferSpaceOwnershipResponse transferOwnership(String id, TransferOwnershipRequest request)
```

```java
TransferSpaceOwnershipResponse transferOwnership(ai.pairsys.goodmem.client.models.SpaceId id, TransferOwnershipRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
TransferSpaceOwnershipResponse transferOwnership(java.util.UUID id, TransferOwnershipRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceId](../models/SpaceId.md)
- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
