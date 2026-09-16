<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# EmbedderCreationRequest

Request body for creating a new Embedder. An Embedder represents a configuration for vectorizing content.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): User-facing name of the embedder
- `description` (`String`): Description of the embedder
- `providerType` (`ProviderType`): Type of embedding provider
- `endpointUrl` (`String`): Base HTTP(S) endpoint for provider requests. Gemini endpoint URLs must not contain query parameters.
- `apiPath` (`String`): Provider-relative request path. Omit or send blank to use the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
- `modelIdentifier` (`String`): Model identifier
- `dimensionality` (`Integer`): Output vector dimensions
- `distributionType` (`DistributionType`): Type of embedding distribution (DENSE or SPARSE)
- `maxSequenceLength` (`Integer`): Maximum input sequence length
- `supportedModalities` (`java.util.List<Modality>`): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`java.util.Map<String, String>`): User-defined labels for categorization
- `version` (`String`): Version information
- `monitoringEndpoint` (`String`): Monitoring endpoint URL
- `ownerId` (`UserId`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_EMBEDDER is evaluated against the proposed embedder and owner. Typed wrapper `UserId`; build from a raw string with `UserId.from(String)`.
- `embedderId` (`EmbedderId`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. Typed wrapper `EmbedderId`; build from a raw string with `EmbedderId.from(String)`.
- `dashscopeApiDialect` (`DashScopeApiDialect`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native text default. Allowed values for this field: `EMBEDDING_NATIVE_TEXT`, `EMBEDDING_NATIVE_CONTENTS`, `OPENAI_COMPATIBLE`.
- `geminiEndpointConfig` (`GeminiEndpointConfig`): Gemini backend routing. Valid only for the GEMINI provider. Omit to use the Developer API; when present, backend is required and the gRPC service validates the backend-specific projectId and location contract.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EmbedderId](EmbedderId.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
- [UserId](UserId.md)
