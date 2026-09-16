<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# GeminiEndpointConfig

Gemini backend routing. DEVELOPER does not use projectId or location; GOOGLE_CLOUD requires projectId and defaults an omitted location to global.

`Goodmem.Client.Models.GeminiEndpointConfig`

- `Backend` (`GeminiApiBackend`, required): Google API surface. UNSPECIFIED is invalid when this configuration is supplied on a write. JSON: `backend`.
- `Location` (`string?`): Google Cloud location. Valid only for GOOGLE_CLOUD; omission defaults to global. JSON: `location`.
- `ProjectId` (`string?`): Google Cloud resource project. Required for GOOGLE_CLOUD and unused for DEVELOPER; this is distinct from the ADC quota project. JSON: `projectId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [GeminiApiBackend](GeminiApiBackend.md)
