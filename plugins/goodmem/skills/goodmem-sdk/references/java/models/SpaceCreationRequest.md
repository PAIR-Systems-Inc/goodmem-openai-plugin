<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# SpaceCreationRequest

Request body for creating a new Space. A Space is a container for organizing related memories with vector embeddings.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `name` (`String`): The desired name for the space. Must be unique within the user's scope.
- `labels` (`java.util.Map<String, String>`): A set of key-value pairs to categorize or tag the space. Used for filtering and organizational purposes.
- `spaceEmbedders` (`java.util.List<SpaceEmbedderConfig>`): List of embedder configurations to associate with this space. At least one embedder configuration is required. Each specifies an embedder ID and a relative default retrieval weight used when no per-request overrides are provided.
- `ownerId` (`UserId`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_SPACE is evaluated against the proposed space and owner. Typed wrapper `UserId`; build from a raw string with `UserId.from(String)`.
- `defaultChunkingConfig` (`ChunkingConfiguration`): Default chunking strategy for memories in this space
- `spaceId` (`SpaceId`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. Typed wrapper `SpaceId`; build from a raw string with `SpaceId.from(String)`.

[Java](../../java.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [SpaceEmbedderConfig](SpaceEmbedderConfig.md)
- [SpaceId](SpaceId.md)
- [UserId](UserId.md)
