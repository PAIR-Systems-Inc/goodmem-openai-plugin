<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbedderCreationRequest

Request body for creating a new Embedder. An Embedder represents a configuration for vectorizing content.

- `displayName` (`string`, required): User-facing name of the embedder
- `description` (`string | null`, optional): Description of the embedder
- `providerType` (`ProviderType`, required): Type of embedding provider
- `endpointUrl` (`string`, required): Base HTTP(S) endpoint for provider requests. Gemini endpoint URLs must not contain query parameters.
- `apiPath` (`string | null`, optional): Provider-relative request path. Omit or send blank to use the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
- `modelIdentifier` (`string`, required): Model identifier
- `dimensionality` (`number`, required): Output vector dimensions
- `distributionType` (`DistributionType`, required): Type of embedding distribution (DENSE or SPARSE)
- `maxSequenceLength` (`number | null`, optional): Maximum input sequence length
- `supportedModalities` (`Array<Modality> | null`, optional): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication | null`, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`Record<string, string> | null`, optional): User-defined labels for categorization
- `version` (`string | null`, optional): Version information
- `monitoringEndpoint` (`string | null`, optional): Monitoring endpoint URL
- `ownerId` (`string | null`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_EMBEDDER is evaluated against the proposed embedder and owner.
- `embedderId` (`string | null`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native text default. Allowed values for this field: EMBEDDING_NATIVE_TEXT, EMBEDDING_NATIVE_CONTENTS, OPENAI_COMPATIBLE.
- `geminiEndpointConfig` (`GeminiEndpointConfig | null`, optional): Gemini backend routing. Valid only for the GEMINI provider. Omit to use the Developer API; when present, backend is required and the gRPC service validates the backend-specific projectId and location contract.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
