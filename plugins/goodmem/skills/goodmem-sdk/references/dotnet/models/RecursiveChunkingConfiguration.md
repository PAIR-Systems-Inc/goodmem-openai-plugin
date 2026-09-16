<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RecursiveChunkingConfiguration

Recursive hierarchical chunking strategy with configurable separators and overlap

`Goodmem.Client.Models.RecursiveChunkingConfiguration`

- `ChunkOverlap` (`int`, required): Sliding overlap between chunks JSON: `chunkOverlap`.
- `ChunkSize` (`int`, required): Maximum size of a chunk (should be ≤ context window) JSON: `chunkSize`.
- `KeepStrategy` (`SeparatorKeepStrategy`, required): How to handle separators after splitting. KEEP_NONE is deprecated and behaves as KEEP_END. JSON: `keepStrategy`.
- `LengthMeasurement` (`LengthMeasurement`, required): How to measure chunk length JSON: `lengthMeasurement`.
- `SeparatorIsRegex` (`bool?`): Whether separators are regex patterns JSON: `separatorIsRegex`.
- `Separators` (`IReadOnlyList<string>?`): Hierarchical separator list (order = preference) JSON: `separators`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
- [SeparatorKeepStrategy](SeparatorKeepStrategy.md)
