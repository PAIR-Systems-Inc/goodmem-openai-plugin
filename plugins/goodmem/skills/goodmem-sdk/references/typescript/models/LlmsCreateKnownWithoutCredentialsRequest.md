<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LlmsCreateKnownWithoutCredentialsRequest

```ts

export type LlmsCreateKnownWithoutCredentialsRequest = Prettify<Partial<Omit<LLMCreationRequest, "displayName" | "modelIdentifier" | "credentials">> & {
    displayName: LLMCreationRequest["displayName"];
    modelIdentifier: LlmModelIdentifier;
    credentials?: null | undefined;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LLMCreationRequest](LLMCreationRequest.md)
- [LlmModelIdentifier](LlmModelIdentifier.md)
- [Prettify](Prettify.md)
