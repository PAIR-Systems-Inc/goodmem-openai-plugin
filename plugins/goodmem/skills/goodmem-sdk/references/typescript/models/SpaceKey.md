<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpaceKey

Space configuration for retrieval operations with optional embedder weight overrides.

- `spaceId` (`string`, required): The UUID for the space to search.
- `embedderWeights` (`Array<EmbedderWeight> | null`, optional): Optional per-embedder weight overrides for this space. If not specified, database defaults are used.
- `filter` (`string | null`, optional): Optional filter expression that must evaluate to true for memories in this space.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbedderWeight](EmbedderWeight.md)
