<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# SpaceKey

Space configuration for retrieval operations with optional embedder weight overrides.

- `spaceId` (`SpaceId`): The UUID for the space to search. Typed wrapper `SpaceId`; build from a raw string with `SpaceId.from(String)`.
- `embedderWeights` (`java.util.List<EmbedderWeight>`): Optional per-embedder weight overrides for this space. If not specified, database defaults are used.
- `filter` (`String`): Optional filter expression that must evaluate to true for memories in this space.

[Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderWeight](EmbedderWeight.md)
- [SpaceId](SpaceId.md)
