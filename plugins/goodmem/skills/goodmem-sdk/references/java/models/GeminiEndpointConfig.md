<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# GeminiEndpointConfig

Gemini backend routing. DEVELOPER does not use projectId or location; GOOGLE_CLOUD requires projectId and defaults an omitted location to global.

- `backend` (`GeminiApiBackend`): Google API surface. UNSPECIFIED is invalid when this configuration is supplied on a write.
- `projectId` (`ProjectId`): Google Cloud resource project. Required for GOOGLE_CLOUD and unused for DEVELOPER; this is distinct from the ADC quota project. Typed wrapper `ProjectId`; build from a raw string with `ProjectId.from(String)`.
- `location` (`String`): Google Cloud location. Valid only for GOOGLE_CLOUD; omission defaults to global.

[Java](../../java.md)

Related types — open only those used by your request:

- [GeminiApiBackend](GeminiApiBackend.md)
- [ProjectId](ProjectId.md)
