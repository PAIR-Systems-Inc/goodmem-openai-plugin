<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpaceEmbedderConfig

Configuration for associating an embedder with a space.

- `embedderId` (`string`, required): The UUID for the embedder to associate with the space.
- `defaultRetrievalWeight` (`number | null`, optional): Relative weight for this embedder used by default during retrieval. If omitted, defaults to 1.0; values need not sum to 1 and can be overridden per request.

[TypeScript](../../typescript.md)
