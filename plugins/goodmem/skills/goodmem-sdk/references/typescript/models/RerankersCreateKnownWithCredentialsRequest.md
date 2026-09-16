<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RerankersCreateKnownWithCredentialsRequest

```ts

export type RerankersCreateKnownWithCredentialsRequest = Prettify<Partial<Omit<RerankerCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: RerankerCreationRequest["displayName"];
    modelIdentifier: RerankerModelIdentifier;
    credentials: EndpointAuthentication;
}>;
```

Effective request fields (including inherited fields and overrides):

- `apiPath` (`string | null | undefined`, optional): API path for reranking request (defaults: Cohere /v2/rerank, Jina /v1/rerank, others /rerank)
- `credentials` (`EndpointAuthentication`, required):
- `dashscopeApiDialect` (`DashScopeApiDialect | null | undefined`, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from apiPath, the model catalog, or the native reranking default. Allowed values for this field: RERANK_NATIVE_NESTED, RERANK_COMPATIBLE_FLAT.
- `description` (`string | null | undefined`, optional): Description of the reranker
- `displayName` (`string`, required):
- `endpointUrl` (`string | undefined`, optional): API endpoint URL
- `labels` (`Record<string, string> | null | undefined`, optional): User-defined labels for categorization
- `modelIdentifier` (`RerankerModelIdentifier`, required):
- `monitoringEndpoint` (`string | null | undefined`, optional): Monitoring endpoint URL
- `ownerId` (`string | null | undefined`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_RERANKER is evaluated against the proposed reranker and owner.
- `providerType` (`ProviderType | undefined`, optional): Type of reranking provider. Allowed values for this field: VLLM, TEI, LLAMA_CPP, VOYAGE, COHERE, JINA, DASHSCOPE.
- `rerankerId` (`string | null | undefined`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
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
- [EndpointAuthentication](EndpointAuthentication.md)
- [Modality](Modality.md)
- [ProviderType](ProviderType.md)
- [RerankerCreationRequest](RerankerCreationRequest.md)
- [RerankerModelIdentifier](RerankerModelIdentifier.md)
