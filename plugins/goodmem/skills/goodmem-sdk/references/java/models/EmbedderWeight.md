<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# EmbedderWeight

Per-embedder weight override for retrieval operations.

- `embedderId` (`EmbedderId`): The UUID for the embedder. Typed wrapper `EmbedderId`; build from a raw string with `EmbedderId.from(String)`.
- `weight` (`Double`): The weight to apply to this embedder's results. Can be positive, negative, or zero.

[Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderId](EmbedderId.md)
