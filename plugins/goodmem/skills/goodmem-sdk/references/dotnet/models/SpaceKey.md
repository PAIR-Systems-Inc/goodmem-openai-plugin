<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# SpaceKey

Space configuration for retrieval operations with optional embedder weight overrides.

`Goodmem.Client.Models.SpaceKey`

- `EmbedderWeights` (`IReadOnlyList<EmbedderWeight>?`): Optional per-embedder weight overrides for this space. If not specified, database defaults are used. JSON: `embedderWeights`.
- `Filter` (`string?`): Optional filter expression that must evaluate to true for memories in this space. JSON: `filter`.
- `SpaceId` (`string`, required): The UUID for the space to search. JSON: `spaceId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [EmbedderWeight](EmbedderWeight.md)
