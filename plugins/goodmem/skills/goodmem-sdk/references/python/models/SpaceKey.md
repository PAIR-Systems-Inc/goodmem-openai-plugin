<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# SpaceKey

Space configuration for retrieval operations with optional embedder weight overrides.

- `space_id` (`str`, required): The UUID for the space to search. JSON: `spaceId`.
- `embedder_weights` (`list[EmbedderWeight] | None`, optional): Optional per-embedder weight overrides for this space. If not specified, database defaults are used. JSON: `embedderWeights`.
- `filter` (`str | None`, optional): Optional filter expression that must evaluate to true for memories in this space.

[Python](../../python.md)

Related types — open only those used by your request:

- [EmbedderWeight](EmbedderWeight.md)
