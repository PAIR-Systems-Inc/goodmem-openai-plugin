<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMCreationRequest

Request body for creating a new LLM. An LLM represents a configuration for text generation services.

- `displayName` (`string`, required): User-facing name of the LLM
- `description` (`string | null`, optional): Description of the LLM
- `providerType` (`LLMProviderType`, required): Type of LLM provider
- `endpointUrl` (`string`, required): API endpoint base URL (OpenAI-compatible base, typically ends with /v1)
- `apiPath` (`string | null`, optional): API path for chat/completions request (defaults to /chat/completions if not provided)
- `modelIdentifier` (`string`, required): Model identifier
- `supportedModalities` (`Array<Modality> | null`, optional): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication | null`, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`Record<string, string> | null`, optional): User-defined labels for categorization
- `version` (`string | null`, optional): Version information
- `monitoringEndpoint` (`string | null`, optional): Monitoring endpoint URL
- `capabilities` (`LLMCapabilities | null`, optional): LLM capabilities defining supported features and modes. Optional - server infers capabilities from model identifier if not provided.
- `defaultSamplingParams` (`LLMSamplingParams | null`, optional): Default sampling parameters for generation requests
- `maxContextLength` (`number | null`, optional): Maximum context window size in tokens
- `clientConfig` (`Record<string, unknown> | null`, optional): Provider-specific client configuration as flexible JSON structure
- `ownerId` (`string | null`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_LLM is evaluated against the proposed LLM and owner.
- `llmId` (`string | null`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. When omitted, a recognized apiPath determines the dialect; otherwise OPENAI_COMPATIBLE is used. Allowed values for this field: LLM_NATIVE_TEXT, LLM_NATIVE_MULTIMODAL, OPENAI_COMPATIBLE.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMProviderType](LLMProviderType.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [Modality](Modality.md)
