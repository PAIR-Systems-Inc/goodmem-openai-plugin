<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateEmbedderRequest

Request body for updating an existing Embedder. Only fields that should be updated need to be included. supportedModalities is creation-time only and cannot be changed here.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): User-facing name of the embedder
- `description` (`String`): Description of the embedder
- `endpointUrl` (`String`): Replacement base HTTP(S) endpoint. Omit to preserve the stored value. Gemini endpoint URLs must not contain query parameters.
- `apiPath` (`String`): Replacement provider-relative request path. Omit to preserve the stored value, except that changing the Gemini backend without apiPath selects that backend's default; send blank to restore the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
- `modelIdentifier` (`String`): Model identifier
- `dimensionality` (`Integer`): Output vector dimensions
- `distributionType` (`DistributionType`): Type of embedding distribution (DENSE or SPARSE)
- `maxSequenceLength` (`Integer`): Maximum input sequence length
- `credentials` (`EndpointAuthentication`): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replaceLabels` (`java.util.Map<String, String>`): Replace all existing labels with these (mutually exclusive with mergeLabels)
- `mergeLabels` (`java.util.Map<String, String>`): Merge these labels with existing ones (mutually exclusive with replaceLabels)
- `version` (`String`): Version information
- `monitoringEndpoint` (`String`): Monitoring endpoint URL
- `dashscopeApiDialect` (`DashScopeApiDialect`): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: `EMBEDDING_NATIVE_TEXT`, `EMBEDDING_NATIVE_CONTENTS`, `OPENAI_COMPATIBLE`.
- `geminiEndpointConfig` (`GeminiEndpointConfig`): When present, atomically replaces the complete Gemini backend routing configuration. Valid only for a GEMINI embedder. Omit to preserve the stored configuration; the gRPC service validates the backend-specific projectId and location contract.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
