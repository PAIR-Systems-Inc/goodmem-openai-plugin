<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateEmbedderRequestBase

- `displayName` (`string | null`, optional): User-facing name of the embedder
- `description` (`string | null`, optional): Description of the embedder
- `endpointUrl` (`string | null`, optional): Replacement base HTTP(S) endpoint. Omit to preserve the stored value. Gemini endpoint URLs must not contain query parameters.
- `apiPath` (`string | null`, optional): Replacement provider-relative request path. Omit to preserve the stored value, except that changing the Gemini backend without apiPath selects that backend's default; send blank to restore the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
- `modelIdentifier` (`string | null`, optional): Model identifier
- `dimensionality` (`number | null`, optional): Output vector dimensions
- `distributionType` (`DistributionType | null`, optional): Type of embedding distribution (DENSE or SPARSE)
- `maxSequenceLength` (`number | null`, optional): Maximum input sequence length
- `credentials` (`EndpointAuthentication | null`, optional): Replace stored credentials. Omit this field to preserve the current credentials; a present empty payload is invalid and never clears them.
- `replaceLabels` (`Record<string, string> | null`, optional): Replace all existing labels with these (mutually exclusive with mergeLabels)
- `mergeLabels` (`Record<string, string> | null`, optional): Merge these labels with existing ones (mutually exclusive with replaceLabels)
- `version` (`string | null`, optional): Version information
- `monitoringEndpoint` (`string | null`, optional): Monitoring endpoint URL
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): Update the DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to preserve the stored dialect. Changing apiPath to a recognized canonical DashScope dialect infers its matching dialect; a custom path preserves an existing dialect, while a legacy null dialect is inferred. Allowed values for this field: EMBEDDING_NATIVE_TEXT, EMBEDDING_NATIVE_CONTENTS, OPENAI_COMPATIBLE.
- `geminiEndpointConfig` (`GeminiEndpointConfig | null`, optional): When present, atomically replaces the complete Gemini backend routing configuration. Valid only for a GEMINI embedder. Omit to preserve the stored configuration; the gRPC service validates the backend-specific projectId and location contract.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
