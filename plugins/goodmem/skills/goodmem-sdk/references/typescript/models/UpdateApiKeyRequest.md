<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateApiKeyRequest

Request parameters for updating an API key.

```ts

export type UpdateApiKeyRequest = AtMostOne<UpdateApiKeyRequestBase, "replaceLabels" | "mergeLabels">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AtMostOne](AtMostOne.md)
- [UpdateApiKeyRequestBase](UpdateApiKeyRequestBase.md)
