<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# SentenceChunkingConfiguration

Sentence-based chunking strategy with language detection support

`Goodmem.Client.Models.SentenceChunkingConfiguration`

- `EnableLanguageDetection` (`bool?`): Whether to detect language for better segmentation JSON: `enableLanguageDetection`.
- `LengthMeasurement` (`LengthMeasurement`, required): How to measure chunk length JSON: `lengthMeasurement`.
- `MaxChunkSize` (`int`, required): Maximum size of a chunk JSON: `maxChunkSize`.
- `MinChunkSize` (`int`, required): Minimum size before creating a new chunk JSON: `minChunkSize`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
