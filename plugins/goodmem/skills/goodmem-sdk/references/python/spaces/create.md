<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.create

Create a new Space

Creates a new space with the provided name, labels, and embedder configuration. A space is a container for organizing related memories.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless owner_id is provided; CREATE_SPACE is evaluated against the proposed space and owner.

EMBEDDER REQUIREMENTS: At least one embedder configuration must be specified. Every referenced embedder must exist, and the caller must have EXECUTE_EMBEDDER on each one.

DUPLICATE DETECTION: Returns ALREADY_EXISTS if another space exists with identical {owner_id, name} (case-sensitive). This operation is NOT idempotent.

Args:
    name (str): The desired name for the space. Must be unique within the user's scope.
    space_embedders (list[SpaceEmbedderConfig]): List of embedder configurations to associate with this space. At least one embedder configuration is required. Each specifies an embedder ID and a relative default retrieval weight used when no per-request overrides are provided.
    default_chunking_config (ChunkingConfiguration, optional, SDK default={"recursive":{"chunkSize":512,"chunkOverlap":64,"keepStrategy":"KEEP_END","lengthMeasurement":"CHARACTER_COUNT"}}): Default strategy to chunk any memory ingested into this space. Can be overridden by per-memory chunking strategy.
    labels (dict[str, str], optional): A set of key-value pairs to categorize or tag the space. Used for filtering and organizational purposes.
    owner_id (str, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_SPACE is evaluated against the proposed space and owner.
    space_id (str, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.

Returns:
    Space

```python
spaces.create(*, name: 'str', space_embedders: 'list[SpaceEmbedderConfig]', default_chunking_config: 'ChunkingConfiguration' = {'recursive': {'chunkSize': 512, 'chunkOverlap': 64, 'keepStrategy': 'KEEP_END', 'lengthMeasurement': 'CHARACTER_COUNT'}}, labels: 'dict[str, str] | None' = None, owner_id: 'str | None' = None, space_id: 'str | None' = None) -> 'Space'
```

[spaces](../spaces.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](../models/ChunkingConfiguration.md)
- [SpaceEmbedderConfig](../models/SpaceEmbedderConfig.md)
