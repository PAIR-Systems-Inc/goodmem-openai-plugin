<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpaceCreationRequest

Request body for creating a new Space. A Space is a container for organizing related memories with vector embeddings.

- `name` (`string`, required): The desired name for the space. Must be unique within the user's scope.
- `labels` (`Record<string, string> | null`, optional): A set of key-value pairs to categorize or tag the space. Used for filtering and organizational purposes.
- `spaceEmbedders` (`[SpaceEmbedderConfig, ...SpaceEmbedderConfig[]]`, required): List of embedder configurations to associate with this space. At least one embedder configuration is required. Each specifies an embedder ID and a relative default retrieval weight used when no per-request overrides are provided.
- `ownerId` (`string | null`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_SPACE is evaluated against the proposed space and owner.
- `defaultChunkingConfig` (`ChunkingConfiguration`, required): Default chunking strategy for memories in this space
- `spaceId` (`string | null`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [SpaceEmbedderConfig](SpaceEmbedderConfig.md)
