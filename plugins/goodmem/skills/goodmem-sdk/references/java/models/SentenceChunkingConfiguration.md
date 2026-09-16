<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# SentenceChunkingConfiguration

Sentence-based chunking strategy with language detection support

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `maxChunkSize` (`Integer`): Maximum size of a chunk
- `minChunkSize` (`Integer`): Minimum size before creating a new chunk
- `enableLanguageDetection` (`Boolean`): Whether to detect language for better segmentation
- `lengthMeasurement` (`LengthMeasurement`): How to measure chunk length

[Java](../../java.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
