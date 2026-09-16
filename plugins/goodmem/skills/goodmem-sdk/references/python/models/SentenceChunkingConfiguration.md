<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# SentenceChunkingConfiguration

Sentence-based chunking strategy with language detection support

- `max_chunk_size` (`int`, required): Maximum size of a chunk JSON: `maxChunkSize`.
- `min_chunk_size` (`int`, required): Minimum size before creating a new chunk JSON: `minChunkSize`.
- `enable_language_detection` (`bool | None`, optional): Whether to detect language for better segmentation JSON: `enableLanguageDetection`.
- `length_measurement` (`LengthMeasurement | None`, required): How to measure chunk length JSON: `lengthMeasurement`.

[Python](../../python.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
