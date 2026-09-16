<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ContextItem

Context item with either text or binary content.

```ts

export type ContextItem = RequireExactlyOne<ContextItemBase, "binary" | "text">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ContextItemBase](ContextItemBase.md)
- [RequireExactlyOne](RequireExactlyOne.md)
