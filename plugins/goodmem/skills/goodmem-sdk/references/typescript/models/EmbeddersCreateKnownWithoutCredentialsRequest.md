<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbeddersCreateKnownWithoutCredentialsRequest

```ts

export type EmbeddersCreateKnownWithoutCredentialsRequest = Prettify<Partial<Omit<EmbedderCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: EmbedderCreationRequest["displayName"];
    modelIdentifier: EmbedderModelIdentifier;
    credentials?: null | undefined;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbedderCreationRequest](EmbedderCreationRequest.md)
- [EmbedderModelIdentifier](EmbedderModelIdentifier.md)
- [Prettify](Prettify.md)
