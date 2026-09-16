<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMUpdateRequestBase

- `displayName` (`string | null`, optional): Update display name
- `description` (`string | null`, optional): Update description
- `endpointUrl` (`string | null`, optional): Update endpoint base URL (OpenAI-compatible base, typically ends with /v1)
- `apiPath` (`string | null`, optional): Update API path
- `modelIdentifier` (`string | null`, optional): Update model identifier (cannot be empty)
- `supportedModalities` (`Array<Modality> | null`, optional): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself)
- `credentials` (`EndpointAuthentication | null`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `version` (`string | null`, optional): Update version information
- `monitoringEndpoint` (`string | null`, optional): Update monitoring endpoint URL
- `capabilities` (`LLMCapabilities | null`, optional): Update LLM capabilities (replaces entire capability set; clients MUST send all flags)
- `defaultSamplingParams` (`LLMSamplingParams | null`, optional): Update default sampling parameters
- `maxContextLength` (`number | null`, optional): Update maximum context window size in tokens
- `clientConfig` (`Record<string, unknown> | null`, optional): Update provider-specific client configuration (replaces entire config; no merging)
- `replaceLabels` (`Record<string, string> | null`, optional): Replace all existing labels with this set. Empty map clears all labels. Cannot be used with mergeLabels.
- `mergeLabels` (`Record<string, string> | null`, optional): Merge with existing labels: upserts with overwrite. Labels not mentioned are preserved. Cannot be used with replaceLabels.
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: LLM_NATIVE_TEXT, LLM_NATIVE_MULTIMODAL, OPENAI_COMPATIBLE.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [Modality](Modality.md)
