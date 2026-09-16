<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LlmsCreateKnownWithoutCredentialsRequest

```ts

export type LlmsCreateKnownWithoutCredentialsRequest = Prettify<Partial<Omit<LLMCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: LLMCreationRequest["displayName"];
    modelIdentifier: LlmModelIdentifier;
    credentials?: null | undefined;
}>;
```

Effective request fields (including inherited fields and overrides):

- `apiPath` (`string | null | undefined`, optional): API path for chat/completions request (defaults to /chat/completions if not provided)
- `capabilities` (`LLMCapabilities | null | undefined`, optional): LLM capabilities defining supported features and modes. Optional - server infers capabilities from model identifier if not provided.
- `clientConfig` (`Record<string, unknown> | null | undefined`, optional): Provider-specific client configuration as flexible JSON structure
- `credentials` (`null | undefined`, optional):
- `dashscopeApiDialect` (`DashScopeApiDialect | null | undefined`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. When omitted, a recognized apiPath determines the dialect; otherwise OPENAI_COMPATIBLE is used. Allowed values for this field: LLM_NATIVE_TEXT, LLM_NATIVE_MULTIMODAL, OPENAI_COMPATIBLE.
- `defaultSamplingParams` (`LLMSamplingParams | null | undefined`, optional): Default sampling parameters for generation requests
- `description` (`string | null | undefined`, optional): Description of the LLM
- `displayName` (`string`, required):
- `endpointUrl` (`string | undefined`, optional): API endpoint base URL (OpenAI-compatible base, typically ends with /v1)
- `labels` (`Record<string, string> | null | undefined`, optional): User-defined labels for categorization
- `llmId` (`string | null | undefined`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
- `maxContextLength` (`number | null | undefined`, optional): Maximum context window size in tokens
- `modelIdentifier` (`LlmModelIdentifier`, required):
- `monitoringEndpoint` (`string | null | undefined`, optional): Monitoring endpoint URL
- `ownerId` (`string | null | undefined`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_LLM is evaluated against the proposed LLM and owner.
- `providerType` (`LLMProviderType | undefined`, optional): Type of LLM provider
- `supportedModalities` (`Modality[] | null | undefined`, optional): Supported content modalities (defaults to TEXT if not provided)
- `version` (`string | null | undefined`, optional): Version information

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMCreationRequest](LLMCreationRequest.md)
- [LLMProviderType](LLMProviderType.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [LlmModelIdentifier](LlmModelIdentifier.md)
- [Modality](Modality.md)
