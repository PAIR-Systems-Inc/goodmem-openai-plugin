<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# ChunkingConfiguration

Configuration for text chunking strategy used when processing content. Exactly one of none, recursive, or sentence must be provided.

- `none` (`NoChunkingConfiguration | None`, optional): No chunking strategy - preserve original content as single unit
- `recursive` (`RecursiveChunkingConfiguration | None`, optional): Recursive hierarchical chunking strategy with configurable separators
- `sentence` (`SentenceChunkingConfiguration | None`, optional): Sentence-based chunking strategy with language detection

[Python](../../python.md)

Related types — open only those used by your request:

- [NoChunkingConfiguration](NoChunkingConfiguration.md)
- [RecursiveChunkingConfiguration](RecursiveChunkingConfiguration.md)
- [SentenceChunkingConfiguration](SentenceChunkingConfiguration.md)
