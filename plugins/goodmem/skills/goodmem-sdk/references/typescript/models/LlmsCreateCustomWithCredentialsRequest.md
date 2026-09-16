<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LlmsCreateCustomWithCredentialsRequest

```ts

export type LlmsCreateCustomWithCredentialsRequest = Prettify<Omit<LLMCreationRequest, "credentials"> & {
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCreationRequest](LLMCreationRequest.md)
- [Prettify](Prettify.md)
