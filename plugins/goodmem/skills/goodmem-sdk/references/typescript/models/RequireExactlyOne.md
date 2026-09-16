<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RequireExactlyOne

```ts

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

- [Prettify](Prettify.md)
