<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RecursiveChunkingConfiguration

Recursive hierarchical chunking strategy with configurable separators and overlap

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `chunkSize` (`Integer`): Maximum size of a chunk (should be \u2264 context window)
- `chunkOverlap` (`Integer`): Sliding overlap between chunks
- `separators` (`java.util.List<String>`): Hierarchical separator list (order = preference)
- `keepStrategy` (`SeparatorKeepStrategy`): How to handle separators after splitting. KEEP_NONE is deprecated and behaves as KEEP_END.
- `separatorIsRegex` (`Boolean`): Whether separators are regex patterns
- `lengthMeasurement` (`LengthMeasurement`): How to measure chunk length

[Java](../../java.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
- [SeparatorKeepStrategy](SeparatorKeepStrategy.md)
