<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateEmbedderRequest

Request body for updating an existing Embedder. Only fields that should be updated need to be included. supportedModalities is creation-time only and cannot be changed here.

`Goodmem.Client.Models.UpdateEmbedderRequest`

- `ApiPath` (`string?`): Replacement provider-relative request path. Omit to preserve the stored value, except that changing the Gemini backend without apiPath selects that backend's default; send blank to restore the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud. JSON: `apiPath`.
- `Credentials` (`EndpointAuthentication?`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: EMBEDDING_NATIVE_TEXT, EMBEDDING_NATIVE_CONTENTS, OPENAI_COMPATIBLE. JSON: `dashscopeApiDialect`.
- `Description` (`string?`): Description of the embedder JSON: `description`.
- `Dimensionality` (`int?`): Output vector dimensions JSON: `dimensionality`.
- `DisplayName` (`string?`): User-facing name of the embedder JSON: `displayName`.
- `DistributionType` (`DistributionType?`): Type of embedding distribution (DENSE or SPARSE) JSON: `distributionType`.
- `EndpointUrl` (`string?`): Replacement base HTTP(S) endpoint. Omit to preserve the stored value. Gemini endpoint URLs must not contain query parameters. JSON: `endpointUrl`.
- `GeminiEndpointConfig` (`GeminiEndpointConfig?`): When present, atomically replaces the complete Gemini backend routing configuration. Valid only for a GEMINI embedder. Omit to preserve the stored configuration; the gRPC service validates the backend-specific projectId and location contract. JSON: `geminiEndpointConfig`.
- `MaxSequenceLength` (`int?`): Maximum input sequence length JSON: `maxSequenceLength`.
- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Merge these labels with existing ones (mutually exclusive with replaceLabels) JSON: `mergeLabels`.
- `ModelIdentifier` (`string?`): Model identifier JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Replace all existing labels with these (mutually exclusive with mergeLabels) JSON: `replaceLabels`.
- `Version` (`string?`): Version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
