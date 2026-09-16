<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.update

Update a space

Updates an existing space with new values for the specified fields. Only name and labels can be updated. Fields not included in the request remain unchanged.

IMMUTABLE FIELDS: space_embedders, default_chunking_config, and ownerId cannot be modified after creation.

NAME UNIQUENESS: Name must be unique per owner - returns ALREADY_EXISTS if name conflicts with an existing space. Requires UPDATE_SPACE on the requested space. This operation is idempotent.

```java
Space update(String id, UpdateSpaceRequest request)
```

```java
Space update(ai.pairsys.goodmem.client.models.SpaceId id, UpdateSpaceRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
Space update(java.util.UUID id, UpdateSpaceRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceId](../models/SpaceId.md)
- [UpdateSpaceRequest](../models/UpdateSpaceRequest.md)
