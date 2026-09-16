<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# llms.list

Retrieves a list of LLM configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_LLM on the GoodMem instance. Each returned LLM must also be visible through READ_LLM; unauthorized LLMs are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

```ts
list(options?: LlmsListOptions, requestOptions?: RequestOptions): Promise<Array<LLMResponseShape>>
```

[llms](../llms.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LlmsListOptions](../models/LlmsListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
