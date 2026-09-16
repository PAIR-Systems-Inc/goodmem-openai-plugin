<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbeddersCreateKnownWithCredentialsRequest

```ts

export type EmbeddersCreateKnownWithCredentialsRequest = Prettify<Partial<Omit<EmbedderCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: EmbedderCreationRequest["displayName"];
    modelIdentifier: EmbedderModelIdentifier;
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbedderCreationRequest](EmbedderCreationRequest.md)
- [EmbedderModelIdentifier](EmbedderModelIdentifier.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Prettify](Prettify.md)
