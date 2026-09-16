<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LLMCreationRequest

Request body for creating a new LLM. An LLM represents a configuration for text generation services.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): User-facing name of the LLM
- `description` (`String`): Description of the LLM
- `providerType` (`LLMProviderType`): Type of LLM provider
- `endpointUrl` (`String`): API endpoint base URL (OpenAI-compatible base, typically ends with /v1)
- `apiPath` (`String`): API path for chat/completions request (defaults to /chat/completions if not provided)
- `modelIdentifier` (`String`): Model identifier
- `supportedModalities` (`java.util.List<Modality>`): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`java.util.Map<String, String>`): User-defined labels for categorization
- `version` (`String`): Version information
- `monitoringEndpoint` (`String`): Monitoring endpoint URL
- `capabilities` (`LLMCapabilities`): LLM capabilities defining supported features and modes. Optional - server infers capabilities from model identifier if not provided.
- `defaultSamplingParams` (`LLMSamplingParams`): Default sampling parameters for generation requests
- `maxContextLength` (`Integer`): Maximum context window size in tokens
- `clientConfig` (`java.util.Map<String, Object>`): Provider-specific client configuration as flexible JSON structure
- `ownerId` (`UserId`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_LLM is evaluated against the proposed LLM and owner. Typed wrapper `UserId`; build from a raw string with `UserId.from(String)`.
- `llmId` (`LlmId`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. Typed wrapper `LlmId`; build from a raw string with `LlmId.from(String)`.
- `dashscopeApiDialect` (`DashScopeApiDialect`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. When omitted, a recognized apiPath determines the dialect; otherwise OPENAI_COMPATIBLE is used. Allowed values for this field: `LLM_NATIVE_TEXT`, `LLM_NATIVE_MULTIMODAL`, `OPENAI_COMPATIBLE`.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMProviderType](LLMProviderType.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [LlmId](LlmId.md)
- [Modality](Modality.md)
- [UserId](UserId.md)
