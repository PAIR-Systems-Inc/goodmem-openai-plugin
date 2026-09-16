<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RerankerCreationRequest

Request body for creating a new Reranker. A Reranker represents a configuration for reranking search results.

- `displayName` (`string`, required): User-facing name of the reranker
- `description` (`string | null`, optional): Description of the reranker
- `providerType` (`ProviderType`, required): Type of reranking provider. Allowed values for this field: VLLM, TEI, LLAMA_CPP, VOYAGE, COHERE, JINA, DASHSCOPE.
- `endpointUrl` (`string`, required): API endpoint URL
- `apiPath` (`string | null`, optional): API path for reranking request (defaults: Cohere /v2/rerank, Jina /v1/rerank, others /rerank)
- `modelIdentifier` (`string`, required): Model identifier
- `supportedModalities` (`Array<Modality> | null`, optional): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication | null`, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`Record<string, string> | null`, optional): User-defined labels for categorization
- `version` (`string | null`, optional): Version information
- `monitoringEndpoint` (`string | null`, optional): Monitoring endpoint URL
- `ownerId` (`string | null`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_RERANKER is evaluated against the proposed reranker and owner.
- `rerankerId` (`string | null`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
- `dashscopeApiDialect` (`DashScopeApiDialect | null`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native reranking default. Allowed values for this field: RERANK_NATIVE_NESTED, RERANK_COMPATIBLE_FLAT.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
