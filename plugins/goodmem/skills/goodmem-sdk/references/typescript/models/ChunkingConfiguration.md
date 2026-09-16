<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ChunkingConfiguration

Configuration for text chunking strategy used when processing content. Exactly one of none, recursive, or sentence must be provided.

```ts

export type ChunkingConfiguration = RequireExactlyOne<ChunkingConfigurationBase, "none" | "recursive" | "sentence">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfigurationBase](ChunkingConfigurationBase.md)
- [RequireExactlyOne](RequireExactlyOne.md)
