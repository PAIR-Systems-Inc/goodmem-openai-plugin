<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateEmbedderRequest

Request body for updating an existing Embedder. Only fields that should be updated need to be included. supportedModalities is creation-time only and cannot be changed here.

- `display_name` (`str | None`, optional): User-facing name of the embedder JSON: `displayName`.
- `description` (`str | None`, optional): Description of the embedder
- `endpoint_url` (`str | None`, optional): Replacement base HTTP(S) endpoint. Omit to preserve the stored value. Gemini endpoint URLs must not contain query parameters. JSON: `endpointUrl`.
- `api_path` (`str | None`, optional): Replacement provider-relative request path. Omit to preserve the stored value, except that changing the Gemini backend without api_path selects that backend's default; send blank to restore the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud. JSON: `apiPath`.
- `model_identifier` (`str | None`, optional): Model identifier JSON: `modelIdentifier`.
- `dimensionality` (`int | None`, optional): Output vector dimensions
- `distribution_type` (`DistributionType | None`, optional): Type of embedding distribution (DENSE or SPARSE) JSON: `distributionType`.
- `max_sequence_length` (`int | None`, optional): Maximum input sequence length JSON: `maxSequenceLength`.
- `credentials` (`EndpointAuthentication | None`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replace_labels` (`dict[str, str] | None`, optional): Replace all existing labels with these (mutually exclusive with merge_labels) JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Merge these labels with existing ones (mutually exclusive with replace_labels) JSON: `mergeLabels`.
- `version` (`str | None`, optional): Version information
- `monitoring_endpoint` (`str | None`, optional): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `dashscope_api_dialect` (`DashScopeApiDialect | None`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing api_path to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. JSON: `dashscopeApiDialect`.
- `gemini_endpoint_config` (`GeminiEndpointConfig | None`, optional): When present, atomically replaces the complete Gemini backend routing configuration. Valid only for a GEMINI embedder. Omit to preserve the stored configuration; the gRPC service validates the backend-specific projectId and location contract. JSON: `geminiEndpointConfig`.

[Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
