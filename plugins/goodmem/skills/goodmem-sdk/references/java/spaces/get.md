<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.get

Get a space by ID

Retrieves a specific space by its unique identifier. Returns the complete space information, including name, labels, embedder configuration, and metadata. Requires READ_SPACE on the requested space. The service distinguishes a missing space from an existing space the caller cannot read. This is a read-only operation safe to retry.

```java
Space get(String id)
```

```java
Space get(ai.pairsys.goodmem.client.models.SpaceId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
Space get(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceId](../models/SpaceId.md)
