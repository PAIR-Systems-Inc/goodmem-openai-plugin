<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# instance.get

Returns singleton instance identity, ownership, and audit metadata after requiring effective READ_INSTANCE authority. The built-in ADMIN role supplies this authority; instance ownership alone does not. A scoped API key must also retain READ_INSTANCE in its immutable ceiling. This operation does not expose credentials or mutate instance state.

```ts
get(requestOptions?: RequestOptions): Promise<GoodMemInstanceResponseShape>
```

[instance](../instance.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
