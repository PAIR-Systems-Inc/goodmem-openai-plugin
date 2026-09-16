<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# SpaceEmbedderConfig

Configuration for associating an embedder with a space.

- `embedderId` (`EmbedderId`): The UUID for the embedder to associate with the space. Typed wrapper `EmbedderId`; build from a raw string with `EmbedderId.from(String)`.
- `defaultRetrievalWeight` (`Double`): Relative weight for this embedder used by default during retrieval. If omitted, defaults to 1.0; values need not sum to 1 and can be overridden per request.

[Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderId](EmbedderId.md)
