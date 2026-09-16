<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# PingOnceRequest

Request payload for a single ping probe

```ts

export type PingOnceRequest = AtMostOne<PingOnceRequestBase, "payload" | "payloadSizeBytes">;
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

- [PingOnceRequestBase](PingOnceRequestBase.md)
