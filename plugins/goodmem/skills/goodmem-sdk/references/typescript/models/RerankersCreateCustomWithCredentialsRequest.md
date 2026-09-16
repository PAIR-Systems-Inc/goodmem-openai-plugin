<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RerankersCreateCustomWithCredentialsRequest

```ts

export type RerankersCreateCustomWithCredentialsRequest = Prettify<Omit<RerankerCreationRequest, "credentials"> & {
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EndpointAuthentication](EndpointAuthentication.md)
- [Prettify](Prettify.md)
- [RerankerCreationRequest](RerankerCreationRequest.md)
