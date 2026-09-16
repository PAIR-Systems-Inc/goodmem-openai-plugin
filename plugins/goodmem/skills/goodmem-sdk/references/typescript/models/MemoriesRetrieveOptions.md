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

Effective request fields (including inherited fields and overrides):

- `chronologicalResort` (`boolean | null | undefined`, optional):
- `context` (`ContextItem[] | null | undefined`, optional): Optional context items (text or binary) to provide additional context for the search.
- `fetchMemory` (`boolean | null | undefined`, optional): Whether to include streamed memory-definition records in the response. Defaults to true when omitted. These records include memory metadata and audit fields, but omit originalContent unless fetchMemoryContent is true.
- `fetchMemoryContent` (`boolean | null | undefined`, optional): Whether streamed memory-definition records include originalContent bytes. Requires fetchMemory=true. Defaults to false when omitted.
- `genTokenBudget` (`number | null | undefined`, optional):
- `hnsw` (`HnswOptions | null | undefined`, optional): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve.
- `llmId` (`string | null | undefined`, optional):
- `llmTemp` (`number | null | undefined`, optional):
- `logging` (`LoggingOptions | null | undefined`, optional): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.callerAttributes to attach if caller opt-in or an admin policy logs the request.
- `maxResults` (`number | null | undefined`, optional):
- `outputBudget` (`TokenBudget | null | undefined`, optional): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget.
- `prompt` (`string | null | undefined`, optional):
- `relevanceThreshold` (`number | null | undefined`, optional):
- `requestedSize` (`number | null | undefined`, optional): Maximum number of memories to retrieve.
- `rerankerId` (`string | null | undefined`, optional):
- `spaceIds` (`[string, ...string[]]`, required):
- `sysPrompt` (`string | null | undefined`, optional):

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ContextItem](ContextItem.md)
- [HnswOptions](HnswOptions.md)
- [LoggingOptions](LoggingOptions.md)
- [MemoriesRetrieveParams](MemoriesRetrieveParams.md)
- [TokenBudget](TokenBudget.md)
