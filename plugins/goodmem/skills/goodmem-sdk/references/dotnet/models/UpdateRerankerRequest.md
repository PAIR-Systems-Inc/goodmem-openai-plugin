<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateRerankerRequest

Request body for updating an existing Reranker. Only fields that should be updated need to be included. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

`Goodmem.Client.Models.UpdateRerankerRequest`

- `ApiPath` (`string?`): API path for reranking request JSON: `apiPath`.
- `Credentials` (`EndpointAuthentication?`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: RERANK_NATIVE_NESTED, RERANK_COMPATIBLE_FLAT. JSON: `dashscopeApiDialect`.
- `Description` (`string?`): Description of the reranker JSON: `description`.
- `DisplayName` (`string?`): User-facing name of the reranker JSON: `displayName`.
- `EndpointUrl` (`string?`): API endpoint URL JSON: `endpointUrl`.
- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Merge these labels with existing ones (mutually exclusive with replaceLabels) JSON: `mergeLabels`.
- `ModelIdentifier` (`string?`): Model identifier JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Replace all existing labels with these (mutually exclusive with mergeLabels) JSON: `replaceLabels`.
- `SupportedModalities` (`IReadOnlyList<Modality>?`): Update supported modalities (if array contains >=1 elements, replaces stored set; if empty or omitted, no change and does not count as an update by itself) JSON: `supportedModalities`.
- `Version` (`string?`): Version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
