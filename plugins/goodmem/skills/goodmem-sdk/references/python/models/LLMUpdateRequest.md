<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# LLMUpdateRequest

Request body for updating an existing LLM. All fields are optional - only specified fields will be updated. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

```python
from goodmem.models import LLMUpdateRequest
```

- `display_name` (`str | None`, optional): Update display name JSON: `displayName`.
- `description` (`str | None`, optional): Update description
- `endpoint_url` (`str | None`, optional): Update endpoint base URL (OpenAI-compatible base, typically ends with /v1) JSON: `endpointUrl`.
- `api_path` (`str | None`, optional): Update API path JSON: `apiPath`.
- `model_identifier` (`str | None`, optional): Update model identifier (cannot be empty) JSON: `modelIdentifier`.
- `supported_modalities` (`list[Modality] | None`, optional): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself) JSON: `supportedModalities`.
- `credentials` (`EndpointAuthentication | None`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `version` (`str | None`, optional): Update version information
- `monitoring_endpoint` (`str | None`, optional): Update monitoring endpoint URL JSON: `monitoringEndpoint`.
- `capabilities` (`LLMCapabilities | None`, optional): Update LLM capabilities (replaces entire capability set; clients MUST send all flags)
- `default_sampling_params` (`LLMSamplingParams | None`, optional): Update default sampling parameters JSON: `defaultSamplingParams`.
- `max_context_length` (`int | None`, optional): Update maximum context window size in tokens JSON: `maxContextLength`.
- `client_config` (`dict[str, Any] | None`, optional): Update provider-specific client configuration (replaces entire config; no merging) JSON: `clientConfig`.
- `replace_labels` (`dict[str, str] | None`, optional): Replace all existing labels with this set. Empty map clears all labels. Cannot be used with merge_labels. JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Merge with existing labels: upserts with overwrite. Labels not mentioned are preserved. Cannot be used with replace_labels. JSON: `mergeLabels`.
- `dashscope_api_dialect` (`DashScopeApiDialect | None`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing api_path to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. JSON: `dashscopeApiDialect`.

[Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCapabilities](LLMCapabilities.md)
- [LLMSamplingParams](LLMSamplingParams.md)
- [Modality](Modality.md)
