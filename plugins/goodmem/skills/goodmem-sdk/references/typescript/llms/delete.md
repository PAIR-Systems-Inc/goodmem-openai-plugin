<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# llms.delete

Permanently deletes an LLM configuration. This operation cannot be undone and removes the LLM record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete any previously generated content using this LLM - existing generations remain accessible. Requires DELETE_LLM on the requested LLM.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[llms](../llms.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
