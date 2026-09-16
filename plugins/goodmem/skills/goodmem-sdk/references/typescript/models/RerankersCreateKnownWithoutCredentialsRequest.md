<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RerankersCreateKnownWithoutCredentialsRequest

```ts

export type RerankersCreateKnownWithoutCredentialsRequest = Prettify<Partial<Omit<RerankerCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: RerankerCreationRequest["displayName"];
    modelIdentifier: RerankerModelIdentifier;
    credentials?: null | undefined;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [Prettify](Prettify.md)
- [RerankerCreationRequest](RerankerCreationRequest.md)
- [RerankerModelIdentifier](RerankerModelIdentifier.md)
