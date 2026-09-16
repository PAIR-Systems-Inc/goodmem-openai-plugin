<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RecursiveChunkingConfiguration

Recursive hierarchical chunking strategy with configurable separators and overlap

- `chunkSize` (`number`, required): Maximum size of a chunk (should be ≤ context window)
- `chunkOverlap` (`number`, required): Sliding overlap between chunks
- `separators` (`Array<string> | null`, optional): Hierarchical separator list (order = preference)
- `keepStrategy` (`SeparatorKeepStrategy`, required): How to handle separators after splitting. KEEP_NONE is deprecated and behaves as KEEP_END.
- `separatorIsRegex` (`boolean | null`, optional): Whether separators are regex patterns
- `lengthMeasurement` (`LengthMeasurement`, required): How to measure chunk length

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
- [SeparatorKeepStrategy](SeparatorKeepStrategy.md)
