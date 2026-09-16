<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# LlmCreationRequest

Request body for creating a new LLM. An LLM represents a configuration for text generation services.

`Goodmem.Client.Models.LlmCreationRequest`

- `ApiPath` (`string?`): API path for chat/completions request (defaults to /chat/completions if not provided) JSON: `apiPath`.
- `Capabilities` (`LlmCapabilities?`): LLM capabilities defining supported features and modes. Optional - server infers capabilities from model identifier if not provided. JSON: `capabilities`.
- `ClientConfig` (`IReadOnlyDictionary<string, object>?`): Provider-specific client configuration as flexible JSON structure JSON: `clientConfig`.
- `Credentials` (`EndpointAuthentication?`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. When omitted, a recognized apiPath determines the dialect; otherwise OPENAI_COMPATIBLE is used. Allowed values for this field: LLM_NATIVE_TEXT, LLM_NATIVE_MULTIMODAL, OPENAI_COMPATIBLE. JSON: `dashscopeApiDialect`.
- `DefaultSamplingParams` (`LlmSamplingParams?`): Default sampling parameters for generation requests JSON: `defaultSamplingParams`.
- `Description` (`string?`): Description of the LLM JSON: `description`.
- `DisplayName` (`string`, required): User-facing name of the LLM JSON: `displayName`.
- `EndpointUrl` (`string?`): API endpoint base URL (OpenAI-compatible base, typically ends with /v1) JSON: `endpointUrl`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): User-defined labels for categorization JSON: `labels`.
- `LlmId` (`string?`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. JSON: `llmId`.
- `MaxContextLength` (`int?`): Maximum context window size in tokens JSON: `maxContextLength`.
- `ModelIdentifier` (`string`, required): Model identifier JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `OwnerId` (`string?`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_LLM is evaluated against the proposed LLM and owner. JSON: `ownerId`.
- `ProviderType` (`LlmProviderType?`): Type of LLM provider JSON: `providerType`.
- `SupportedModalities` (`IReadOnlyList<Modality>?`): Supported content modalities (defaults to TEXT if not provided) JSON: `supportedModalities`.
- `Version` (`string?`): Version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LlmCapabilities](LlmCapabilities.md)
- [LlmProviderType](LlmProviderType.md)
- [LlmSamplingParams](LlmSamplingParams.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
