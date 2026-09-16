<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RerankerCreationRequest

Request body for creating a new Reranker. A Reranker represents a configuration for reranking search results.

`Goodmem.Client.Models.RerankerCreationRequest`

- `ApiPath` (`string?`): API path for reranking request (defaults: Cohere /v2/rerank, Jina /v1/rerank, others /rerank) JSON: `apiPath`.
- `Credentials` (`EndpointAuthentication?`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers. JSON: `credentials`.
- `DashscopeApiDialect` (`DashScopeApiDialect?`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native reranking default. Allowed values for this field: RERANK_NATIVE_NESTED, RERANK_COMPATIBLE_FLAT. JSON: `dashscopeApiDialect`.
- `Description` (`string?`): Description of the reranker JSON: `description`.
- `DisplayName` (`string`, required): User-facing name of the reranker JSON: `displayName`.
- `EndpointUrl` (`string?`): API endpoint URL JSON: `endpointUrl`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): User-defined labels for categorization JSON: `labels`.
- `ModelIdentifier` (`string`, required): Model identifier JSON: `modelIdentifier`.
- `MonitoringEndpoint` (`string?`): Monitoring endpoint URL JSON: `monitoringEndpoint`.
- `OwnerId` (`string?`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_RERANKER is evaluated against the proposed reranker and owner. JSON: `ownerId`.
- `ProviderType` (`ProviderType?`): Type of reranking provider. Allowed values for this field: VLLM, TEI, LLAMA_CPP, VOYAGE, COHERE, JINA, DASHSCOPE. JSON: `providerType`.
- `RerankerId` (`string?`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. JSON: `rerankerId`.
- `SupportedModalities` (`IReadOnlyList<Modality>?`): Supported content modalities (defaults to TEXT if not provided) JSON: `supportedModalities`.
- `Version` (`string?`): Version information JSON: `version`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
