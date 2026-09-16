<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# embedders.list

Retrieves a list of embedder configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_EMBEDDER on the GoodMem instance. Each returned embedder must also be visible through READ_EMBEDDER; unauthorized embedders are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

```ts
list(options?: EmbeddersListOptions, requestOptions?: RequestOptions): Promise<Array<EmbedderResponseShape>>
```

[embedders](../embedders.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [EmbeddersListOptions](../models/EmbeddersListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
