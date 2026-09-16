<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateRerankerRequest

Request body for updating an existing Reranker. Only fields that should be updated need to be included. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

```ts

export type UpdateRerankerRequest = AtMostOne<UpdateRerankerRequestBase, "replaceLabels" | "mergeLabels">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AtMostOne](AtMostOne.md)
- [UpdateRerankerRequestBase](UpdateRerankerRequestBase.md)
