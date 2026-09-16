<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ChunkingConfiguration

Configuration for text chunking strategy used when processing content. Exactly one of none, recursive, or sentence must be provided.

```ts

export type ChunkingConfiguration = RequireExactlyOne<ChunkingConfigurationBase, "none" | "recursive" | "sentence">;
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

- [ChunkingConfigurationBase](ChunkingConfigurationBase.md)
