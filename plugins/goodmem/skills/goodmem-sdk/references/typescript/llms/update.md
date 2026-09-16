<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# llms.update

Updates an existing LLM configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself.

IMPORTANT: providerType is IMMUTABLE after creation and cannot be changed. Requires UPDATE_LLM on the requested LLM.

```ts
update(id: string, request: LLMUpdateRequest, requestOptions?: RequestOptions): Promise<LLMResponseShape>
```

[llms](../llms.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LLMUpdateRequest](../models/LLMUpdateRequest.md)
- [RequestOptions](../models/RequestOptions.md)
