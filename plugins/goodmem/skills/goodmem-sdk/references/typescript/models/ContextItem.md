<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ContextItem

Context item with either text or binary content.

```ts

export type ContextItem = RequireExactlyOne<ContextItemBase, "binary" | "text">;
```

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
export type RequireExactlyOne<T, Keys extends keyof T = keyof T> = Prettify<Omit<T, Keys> & {
    [K in Keys]-?: {
        [P in K]-?: NonNullable<T[P]>;
    } & {
        [P in Exclude<Keys, K>]?: null | undefined;
    };
}[Keys]>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ContextItemBase](ContextItemBase.md)
