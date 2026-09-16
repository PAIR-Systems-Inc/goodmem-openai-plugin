<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# rerankers.get

Retrieves the details of a specific reranker configuration by its unique identifier. Stored credentials are omitted unless includeCredentials is true and the caller also has READ_RERANKER_CREDENTIALS. Requires READ_RERANKER on the requested reranker. The service distinguishes a missing reranker from an existing reranker the caller cannot read. This is a read-only operation with no side effects and is safe to retry.

```ts
get(id: string, options?: RerankersGetOptions, requestOptions?: RequestOptions): Promise<RerankerResponseShape>
```

[rerankers](../rerankers.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [RerankersGetOptions](../models/RerankersGetOptions.md)
