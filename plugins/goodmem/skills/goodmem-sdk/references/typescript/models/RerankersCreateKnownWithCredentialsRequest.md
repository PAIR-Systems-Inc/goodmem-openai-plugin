<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RerankersCreateKnownWithCredentialsRequest

```ts

export type RerankersCreateKnownWithCredentialsRequest = Prettify<Partial<Omit<RerankerCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: RerankerCreationRequest["displayName"];
    modelIdentifier: RerankerModelIdentifier;
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EndpointAuthentication](EndpointAuthentication.md)
- [Prettify](Prettify.md)
- [RerankerCreationRequest](RerankerCreationRequest.md)
- [RerankerModelIdentifier](RerankerModelIdentifier.md)
