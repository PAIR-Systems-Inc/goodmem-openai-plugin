<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# EmbedderCreationRequest

Request body for creating a new Embedder. An Embedder represents a configuration for vectorizing content.

`Goodmem.Client.Models.EmbedderCreationRequest`

- `ApiPath` (`string?`): Provider-relative request path. Omit or send blank to use the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud. JSON: `apiPath`.
- `Credentials` (`EndpointAuthentication?`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native text default. Allowed values for this field: EMBEDDING_NATIVE_TEXT, EMBEDDING_NATIVE_CONTENTS, OPENAI_COMPATIBLE. JSON: `dashscopeApiDialect`.
- `Description` (`string?`): Description of the embedder JSON: `description`.
- `Dimensionality` (`int?`): Output vector dimensions JSON: `dimensionality`.
- `DisplayName` (`string`, required): User-facing name of the embedder JSON: `displayName`.
- `DistributionType` (`DistributionType?`): Type of embedding distribution (DENSE or SPARSE) JSON: `distributionType`.
- `EmbedderId` (`string?`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. JSON: `embedderId`.
- `EndpointUrl` (`string?`): Base HTTP(S) endpoint for provider requests. Gemini endpoint URLs must not contain query parameters. JSON: `endpointUrl`.
- `GeminiEndpointConfig` (`GeminiEndpointConfig?`): Gemini backend routing. Valid only for the GEMINI provider. Omit to use the Developer API; when present, backend is required and the gRPC service validates the backend-specific projectId and location contract. JSON: `geminiEndpointConfig`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): User-defined labels for categorization JSON: `labels`.
- `MaxSequenceLength` (`int?`): Maximum input sequence length JSON: `maxSequenceLength`.
- `ModelIdentifier` (`string`, required): Model identifier JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `OwnerId` (`string?`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_EMBEDDER is evaluated against the proposed embedder and owner. JSON: `ownerId`.
- `ProviderType` (`ProviderType?`): Type of embedding provider JSON: `providerType`.
- `SupportedModalities` (`IReadOnlyList<Modality>?`): Supported content modalities (defaults to TEXT if not provided) JSON: `supportedModalities`.
- `Version` (`string?`): Version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
