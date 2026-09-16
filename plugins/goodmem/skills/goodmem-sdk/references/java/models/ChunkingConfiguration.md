<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ChunkingConfiguration

Configuration for text chunking strategy used when processing content. Exactly one of none, recursive, or sentence must be provided.

- `none` (`NoChunkingConfiguration`): No chunking strategy - preserve original content as single unit
- `recursive` (`RecursiveChunkingConfiguration`): Recursive hierarchical chunking strategy with configurable separators
- `sentence` (`SentenceChunkingConfiguration`): Sentence-based chunking strategy with language detection

[Java](../../java.md)

Related types — open only those used by your request:

- [NoChunkingConfiguration](NoChunkingConfiguration.md)
- [RecursiveChunkingConfiguration](RecursiveChunkingConfiguration.md)
- [SentenceChunkingConfiguration](SentenceChunkingConfiguration.md)
