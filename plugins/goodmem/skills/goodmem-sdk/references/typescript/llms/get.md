<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# llms.get

Retrieves the details of a specific LLM configuration by its unique identifier. Requires READ_LLM on the requested LLM. The service distinguishes a missing LLM from an existing LLM the caller cannot read. This is a read-only operation with no side effects.

```ts
get(id: string, options?: LlmsGetOptions, requestOptions?: RequestOptions): Promise<LLMResponseShape>
```

[llms](../llms.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LlmsGetOptions](../models/LlmsGetOptions.md)
- [RequestOptions](../models/RequestOptions.md)
