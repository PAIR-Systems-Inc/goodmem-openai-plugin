<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateEmbedderRequest

Request body for updating an existing Embedder. Only fields that should be updated need to be included. supportedModalities is creation-time only and cannot be changed here.

```ts

export type UpdateEmbedderRequest = AtMostOne<UpdateEmbedderRequestBase, "replaceLabels" | "mergeLabels">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AtMostOne](AtMostOne.md)
- [UpdateEmbedderRequestBase](UpdateEmbedderRequestBase.md)
