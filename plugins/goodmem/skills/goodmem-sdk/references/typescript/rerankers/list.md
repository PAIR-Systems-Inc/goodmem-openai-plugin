<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# rerankers.list

Retrieves a list of reranker configurations accessible to the caller, with optional filtering.

IMPORTANT: Pagination is NOT supported - all matching results are returned. Results are ordered by created_at descending. Stored credentials are never included in list responses.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_RERANKER on the GoodMem instance. Each returned reranker must also be visible through READ_RERANKER; unauthorized rerankers are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

```ts
list(options?: RerankersListOptions, requestOptions?: RequestOptions): Promise<Array<RerankerResponseShape>>
```

[rerankers](../rerankers.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [RerankersListOptions](../models/RerankersListOptions.md)
