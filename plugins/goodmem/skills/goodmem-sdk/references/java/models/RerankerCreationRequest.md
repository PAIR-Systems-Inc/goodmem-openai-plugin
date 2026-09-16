<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RerankerCreationRequest

Request body for creating a new Reranker. A Reranker represents a configuration for reranking search results.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): User-facing name of the reranker
- `description` (`String`): Description of the reranker
- `providerType` (`ProviderType`): Type of reranking provider. Allowed values for this field: `VLLM`, `TEI`, `LLAMA_CPP`, `VOYAGE`, `COHERE`, `JINA`, `DASHSCOPE`.
- `endpointUrl` (`String`): API endpoint URL
- `apiPath` (`String`): API path for reranking request (defaults: Cohere /v2/rerank, Jina /v1/rerank, others /rerank)
- `modelIdentifier` (`String`): Model identifier
- `supportedModalities` (`java.util.List<Modality>`): Supported content modalities (defaults to TEXT if not provided)
- `credentials` (`EndpointAuthentication`): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
- `labels` (`java.util.Map<String, String>`): User-defined labels for categorization
- `version` (`String`): Version information
- `monitoringEndpoint` (`String`): Monitoring endpoint URL
- `ownerId` (`UserId`): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_RERANKER is evaluated against the proposed reranker and owner. Typed wrapper `UserId`; build from a raw string with `UserId.from(String)`.
- `rerankerId` (`RerankerId`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. Typed wrapper `RerankerId`; build from a raw string with `RerankerId.from(String)`.
- `dashscopeApiDialect` (`DashScopeApiDialect`): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native reranking default. Allowed values for this field: `RERANK_NATIVE_NESTED`, `RERANK_COMPATIBLE_FLAT`.

[Java](../../java.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](DashScopeApiDialect.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
- [RerankerId](RerankerId.md)
- [UserId](UserId.md)
