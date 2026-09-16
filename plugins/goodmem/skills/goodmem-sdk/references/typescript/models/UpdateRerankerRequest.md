<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateRerankerRequest

Request body for updating an existing Reranker. Only fields that should be updated need to be included. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

```ts

export type UpdateRerankerRequest = AtMostOne<UpdateRerankerRequestBase, "replaceLabels" | "mergeLabels">;
```

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type AtMostOne<T, Keys extends keyof T = keyof T> = Prettify<Omit<T, Keys> & ({
    [K in Keys]-?: {
        [P in K]-?: NonNullable<T[P]>;
    } & {
        [P in Exclude<Keys, K>]?: null | undefined;
    };
}[Keys] | {
    [K in Keys]?: null | undefined;
})>;
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [UpdateRerankerRequestBase](UpdateRerankerRequestBase.md)
