<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# LlmUpdateRequest

Request body for updating an existing LLM. All fields are optional - only specified fields will be updated. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

`Goodmem.Client.Models.LlmUpdateRequest`

- `ApiPath` (`string?`): Update API path JSON: `apiPath`.
- `Capabilities` (`LlmCapabilities?`): Update LLM capabilities (replaces entire capability set; clients MUST send all flags) JSON: `capabilities`.
- `ClientConfig` (`IReadOnlyDictionary<string, object>?`): Update provider-specific client configuration (replaces entire config; no merging) JSON: `clientConfig`.
- `Credentials` (`EndpointAuthentication?`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: LLM_NATIVE_TEXT, LLM_NATIVE_MULTIMODAL, OPENAI_COMPATIBLE. JSON: `dashscopeApiDialect`.
- `DefaultSamplingParams` (`LlmSamplingParams?`): Update default sampling parameters JSON: `defaultSamplingParams`.
- `Description` (`string?`): Update description JSON: `description`.
- `DisplayName` (`string?`): Update display name JSON: `displayName`.
- `EndpointUrl` (`string?`): Update endpoint base URL (OpenAI-compatible base, typically ends with /v1) JSON: `endpointUrl`.
- `MaxContextLength` (`int?`): Update maximum context window size in tokens JSON: `maxContextLength`.
- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Merge with existing labels: upserts with overwrite. Labels not mentioned are preserved. Cannot be used with replaceLabels. JSON: `mergeLabels`.
- `ModelIdentifier` (`string?`): Update model identifier (cannot be empty) JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Update monitoring endpoint URL JSON: `monitoringEndpoint`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Replace all existing labels with this set. Empty map clears all labels. Cannot be used with mergeLabels. JSON: `replaceLabels`.
- `SupportedModalities` (`IReadOnlyList<Modality>?`): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself) JSON: `supportedModalities`.
- `Version` (`string?`): Update version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LlmCapabilities](LlmCapabilities.md)
- [LlmSamplingParams](LlmSamplingParams.md)
- [Modality](Modality.md)
