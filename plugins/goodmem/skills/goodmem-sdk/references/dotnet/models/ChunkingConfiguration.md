<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# ChunkingConfiguration

Configuration for text chunking strategy used when processing content. Exactly one of none, recursive, or sentence must be provided.

`Goodmem.Client.Models.ChunkingConfiguration`

- `None` (`NoChunkingConfiguration?`): No chunking strategy - preserve original content as single unit JSON: `none`.
- `Recursive` (`RecursiveChunkingConfiguration?`): Recursive hierarchical chunking strategy with configurable separators JSON: `recursive`.
- `Sentence` (`SentenceChunkingConfiguration?`): Sentence-based chunking strategy with language detection JSON: `sentence`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [NoChunkingConfiguration](NoChunkingConfiguration.md)
- [RecursiveChunkingConfiguration](RecursiveChunkingConfiguration.md)
- [SentenceChunkingConfiguration](SentenceChunkingConfiguration.md)
