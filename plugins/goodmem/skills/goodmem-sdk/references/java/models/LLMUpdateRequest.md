<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LLMUpdateRequest

Request body for updating an existing LLM. All fields are optional - only specified fields will be updated. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): Update display name
- `description` (`String`): Update description
- `endpointUrl` (`String`): Update endpoint base URL (OpenAI-compatible base, typically ends with /v1)
- `apiPath` (`String`): Update API path
- `modelIdentifier` (`String`): Update model identifier (cannot be empty)
- `supportedModalities` (`java.util.List<Modality>`): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself)
- `credentials` (`EndpointAuthentication`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `version` (`String`): Update version information
- `monitoringEndpoint` (`String`): Update monitoring endpoint URL
- `capabilities` (`LLMCapabilities`): Update LLM capabilities (replaces entire capability set; clients MUST send all flags)
- `defaultSamplingParams` (`LLMSamplingParams`): Update default sampling parameters
- `maxContextLength` (`Integer`): Update maximum context window size in tokens
- `clientConfig` (`java.util.Map<String, Object>`): Update provider-specific client configuration (replaces entire config; no merging)
- `replaceLabels` (`java.util.Map<String, String>`): Replace all existing labels with this set. Empty map clears all labels. Cannot be used with mergeLabels.
- `mergeLabels` (`java.util.Map<String, String>`): Merge with existing labels: upserts with overwrite. Labels not mentioned are preserved. Cannot be used with replaceLabels.
- `dashscopeApiDialect` (`DashScopeApiDialect`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: `LLM_NATIVE_TEXT`, `LLM_NATIVE_MULTIMODAL`, `OPENAI_COMPATIBLE`.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [Modality](Modality.md)
