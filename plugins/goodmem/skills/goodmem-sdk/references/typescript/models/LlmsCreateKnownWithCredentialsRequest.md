<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LlmsCreateKnownWithCredentialsRequest

```ts

export type LlmsCreateKnownWithCredentialsRequest = Prettify<Partial<Omit<LLMCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: LLMCreationRequest["displayName"];
    modelIdentifier: LlmModelIdentifier;
    credentials: EndpointAuthentication;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EndpointAuthentication](EndpointAuthentication.md)
- [LLMCreationRequest](LLMCreationRequest.md)
- [LlmModelIdentifier](LlmModelIdentifier.md)
- [Prettify](Prettify.md)
