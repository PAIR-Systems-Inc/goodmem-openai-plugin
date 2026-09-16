<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.create

Create a new Space

Creates a new space with the provided name, labels, and embedder configuration. A space is a container for organizing related memories.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_SPACE is evaluated against the proposed space and owner.

EMBEDDER REQUIREMENTS: At least one embedder configuration must be specified. Every referenced embedder must exist, and the caller must have EXECUTE_EMBEDDER on each one.

DUPLICATE DETECTION: Returns ALREADY_EXISTS if another space exists with identical {ownerId, name} (case-sensitive). This operation is NOT idempotent.

```java
Space create(SpaceCreationRequest request)
```

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceCreationRequest](../models/SpaceCreationRequest.md)
