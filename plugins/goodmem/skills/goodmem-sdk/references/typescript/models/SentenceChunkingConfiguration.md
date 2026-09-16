<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SentenceChunkingConfiguration

Sentence-based chunking strategy with language detection support

- `maxChunkSize` (`number`, required): Maximum size of a chunk
- `minChunkSize` (`number`, required): Minimum size before creating a new chunk
- `enableLanguageDetection` (`boolean | null`, optional): Whether to detect language for better segmentation
- `lengthMeasurement` (`LengthMeasurement`, required): How to measure chunk length

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
