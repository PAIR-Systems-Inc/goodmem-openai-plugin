<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# rerankers.delete

Permanently deletes a reranker configuration. This operation cannot be undone and immediately removes the reranker record from the database.

SIDE EFFECTS: Invalidates any cached references to this reranker; does not affect historical usage data or audit logs. Requires DELETE_RERANKER on the requested reranker. This operation is safe to retry - may return NOT_FOUND if already deleted.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[rerankers](../rerankers.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
