<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AccessPolicyGrantsListOptions

- `resourceKind` (`"INSTANCE" | "USER" | "SERVICE_IDENTITY" | "SPACE" | "API_KEY" | "EMBEDDER" | "RERANKER" | "LLM" | "MEMORY" | "EXTENSION" | "RETRIEVE_MEMORY_LOG_POLICY"`, required): Required target resource kind
- `resourceId` (`string`, optional): Required target UUID except when resourceKind is INSTANCE
- `includeRevoked` (`boolean`, optional): Include revoked history
- `maxResults` (`number`, optional): Page size; 0 or omission uses the default of 50, maximum 1,000
- `nextToken` (`string`, optional): Opaque continuation token

[TypeScript](../../typescript.md)
