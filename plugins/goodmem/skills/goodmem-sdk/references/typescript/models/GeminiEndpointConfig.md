<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# GeminiEndpointConfig

Gemini backend routing. DEVELOPER does not use projectId or location; GOOGLE_CLOUD requires projectId and defaults an omitted location to global.

- `backend` (`GeminiApiBackend`, required): Google API surface. UNSPECIFIED is invalid when this configuration is supplied on a write.
- `projectId` (`string | null`, optional): Google Cloud resource project. Required for GOOGLE_CLOUD and unused for DEVELOPER; this is distinct from the ADC quota project.
- `location` (`string | null`, optional): Google Cloud location. Valid only for GOOGLE_CLOUD; omission defaults to global.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [GeminiApiBackend](GeminiApiBackend.md)
