<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateRerankerRequest

Request body for updating an existing Reranker. Only fields that should be updated need to be included. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

- `display_name` (`str | None`, optional): User-facing name of the reranker JSON: `displayName`.
- `description` (`str | None`, optional): Description of the reranker
- `endpoint_url` (`str | None`, optional): API endpoint URL JSON: `endpointUrl`.
- `api_path` (`str | None`, optional): API path for reranking request JSON: `apiPath`.
- `model_identifier` (`str | None`, optional): Model identifier JSON: `modelIdentifier`.
- `supported_modalities` (`list[Modality] | None`, optional): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself) JSON: `supportedModalities`.
- `credentials` (`EndpointAuthentication | None`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replace_labels` (`dict[str, str] | None`, optional): Replace all existing labels with these (mutually exclusive with merge_labels) JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Merge these labels with existing ones (mutually exclusive with replace_labels) JSON: `mergeLabels`.
- `version` (`str | None`, optional): Version information
- `monitoring_endpoint` (`str | None`, optional): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `dashscope_api_dialect` (`DashScopeApiDialect | None`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing api_path to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. JSON: `dashscopeApiDialect`.

[Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
