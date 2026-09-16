<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoriesRetrieveOptions

```ts

export type MemoriesRetrieveOptions = Prettify<Omit<MemoriesRetrieveParams, "message" | "spaceKeys" | "postProcessor"> & {
    spaceIds: [string, ...string[]];
    llmId?: string | null;
    rerankerId?: string | null;
    llmTemp?: number | null;
    genTokenBudget?: number | null;
    relevanceThreshold?: number | null;
    maxResults?: number | null;
    prompt?: string | null;
    sysPrompt?: string | null;
    chronologicalResort?: boolean | null;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoriesRetrieveParams](MemoriesRetrieveParams.md)
- [Prettify](Prettify.md)
