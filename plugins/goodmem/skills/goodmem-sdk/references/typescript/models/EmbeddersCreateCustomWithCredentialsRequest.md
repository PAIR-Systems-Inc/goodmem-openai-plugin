<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbeddersCreateCustomWithCredentialsRequest

```ts

export type EmbeddersCreateCustomWithCredentialsRequest = Prettify<Omit<EmbedderCreationRequest, "credentials"> & {
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbedderCreationRequest](EmbedderCreationRequest.md)
- [EndpointAuthentication](EndpointAuthentication.md)
- [Prettify](Prettify.md)
