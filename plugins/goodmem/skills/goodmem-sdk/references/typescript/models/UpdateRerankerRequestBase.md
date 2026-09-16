<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateRerankerRequestBase

- `displayName` (`string | null`, optional): User-facing name of the reranker
- `description` (`string | null`, optional): Description of the reranker
- `endpointUrl` (`string | null`, optional): API endpoint URL
- `apiPath` (`string | null`, optional): API path for reranking request
- `modelIdentifier` (`string | null`, optional): Model identifier
- `supportedModalities` (`Array<Modality> | null`, optional): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself)
- `credentials` (`EndpointAuthentication | null`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replaceLabels` (`Record<string, string> | null`, optional): Replace all existing labels with these (mutually exclusive with mergeLabels)
- `mergeLabels` (`Record<string, string> | null`, optional): Merge these labels with existing ones (mutually exclusive with replaceLabels)
- `version` (`string | null`, optional): Version information
- `monitoringEndpoint` (`string | null`, optional): Monitoring endpoint URL
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: RERANK_NATIVE_NESTED, RERANK_COMPATIBLE_FLAT.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
