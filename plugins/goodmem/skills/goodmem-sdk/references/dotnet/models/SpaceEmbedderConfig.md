<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# SpaceEmbedderConfig

Configuration for associating an embedder with a space.

`Goodmem.Client.Models.SpaceEmbedderConfig`

- `DefaultRetrievalWeight` (`double?`): Relative weight for this embedder used by default during retrieval. If omitted, defaults to 1.0; values need not sum to 1 and can be overridden per request. JSON: `defaultRetrievalWeight`.
- `EmbedderId` (`string`, required): The UUID for the embedder to associate with the space. JSON: `embedderId`.

[.NET](../../dotnet.md)
