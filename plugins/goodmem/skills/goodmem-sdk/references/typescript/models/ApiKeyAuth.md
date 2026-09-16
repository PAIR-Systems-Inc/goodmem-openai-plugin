<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ApiKeyAuth

Configuration for classic API-key authentication.

```ts

export type ApiKeyAuth = RequireExactlyOne<ApiKeyAuthBase, "inlineSecret" | "secretRef">;
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

- [ApiKeyAuthBase](ApiKeyAuthBase.md)
