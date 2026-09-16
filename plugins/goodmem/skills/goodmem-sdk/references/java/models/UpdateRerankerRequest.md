<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateRerankerRequest

Request body for updating an existing Reranker. Only fields that should be updated need to be included. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): User-facing name of the reranker
- `description` (`String`): Description of the reranker
- `endpointUrl` (`String`): API endpoint URL
- `apiPath` (`String`): API path for reranking request
- `modelIdentifier` (`String`): Model identifier
- `supportedModalities` (`java.util.List<Modality>`): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself)
- `credentials` (`EndpointAuthentication`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replaceLabels` (`java.util.Map<String, String>`): Replace all existing labels with these (mutually exclusive with mergeLabels)
- `mergeLabels` (`java.util.Map<String, String>`): Merge these labels with existing ones (mutually exclusive with replaceLabels)
- `version` (`String`): Version information
- `monitoringEndpoint` (`String`): Monitoring endpoint URL
- `dashscopeApiDialect` (`DashScopeApiDialect`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: `RERANK_NATIVE_NESTED`, `RERANK_COMPATIBLE_FLAT`.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
