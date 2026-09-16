<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# SpaceCreationRequest

Request body for creating a new Space. A Space is a container for organizing related memories with vector embeddings.

`Goodmem.Client.Models.SpaceCreationRequest`

- `DefaultChunkingConfig` (`ChunkingConfiguration?`): Default chunking strategy for memories in this space JSON: `defaultChunkingConfig`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): A set of key-value pairs to categorize or tag the space. Used for filtering and organizational purposes. JSON: `labels`.
- `Name` (`string`, required): The desired name for the space. Must be unique within the user's scope. JSON: `name`.
- `OwnerId` (`string?`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_SPACE is evaluated against the proposed space and owner. JSON: `ownerId`.
- `SpaceEmbedders` (`IReadOnlyList<SpaceEmbedderConfig>`, required): List of embedder configurations to associate with this space. At least one embedder configuration is required. Each specifies an embedder ID and a relative default retrieval weight used when no per-request overrides are provided. JSON: `spaceEmbedders`.
- `SpaceId` (`string?`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. JSON: `spaceId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [SpaceEmbedderConfig](SpaceEmbedderConfig.md)
