<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AtMostOne

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
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [Prettify](Prettify.md)
