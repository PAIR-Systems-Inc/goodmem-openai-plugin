<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbeddersCreateKnownWithCredentialsRequest

```ts

export type EmbeddersCreateKnownWithCredentialsRequest = Prettify<Partial<Omit<EmbedderCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: EmbedderCreationRequest["displayName"];
    modelIdentifier: EmbedderModelIdentifier;
    credentials: EndpointAuthentication;
}>;
```

Effective request fields (including inherited fields and overrides):

- `apiPath` (`string | null | undefined`, optional): Provider-relative request path. Omit or send blank to use the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
- `credentials` (`EndpointAuthentication`, required):
- `dashscopeApiDialect` (`DashScopeApiDialect | null | undefined`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native text default. Allowed values for this field: EMBEDDING_NATIVE_TEXT, EMBEDDING_NATIVE_CONTENTS, OPENAI_COMPATIBLE.
- `description` (`string | null | undefined`, optional): Description of the embedder
- `dimensionality` (`number | undefined`, optional): Output vector dimensions
- `displayName` (`string`, required):
- `distributionType` (`DistributionType | undefined`, optional): Type of embedding distribution (DENSE or SPARSE)
- `embedderId` (`string | null | undefined`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
- `endpointUrl` (`string | undefined`, optional): Base HTTP(S) endpoint for provider requests. Gemini endpoint URLs must not contain query parameters.
- `geminiEndpointConfig` (`GeminiEndpointConfig | null | undefined`, optional): Gemini backend routing. Valid only for the GEMINI provider. Omit to use the Developer API; when present, backend is required and the gRPC service validates the backend-specific projectId and location contract.
- `labels` (`Record<string, string> | null | undefined`, optional): User-defined labels for categorization
- `maxSequenceLength` (`number | null | undefined`, optional): Maximum input sequence length
- `modelIdentifier` (`EmbedderModelIdentifier`, required):
- `monitoringEndpoint` (`string | null | undefined`, optional): Monitoring endpoint URL
- `ownerId` (`string | null | undefined`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_EMBEDDER is evaluated against the proposed embedder and owner.
- `providerType` (`ProviderType | undefined`, optional): Type of embedding provider
- `supportedModalities` (`Modality[] | null | undefined`, optional): Supported content modalities (defaults to TEXT if not provided)
- `version` (`string | null | undefined`, optional): Version information

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [DistributionType](DistributionType.md)
- [EmbedderCreationRequest](EmbedderCreationRequest.md)
- [EmbedderModelIdentifier](EmbedderModelIdentifier.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [GeminiEndpointConfig](GeminiEndpointConfig.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
