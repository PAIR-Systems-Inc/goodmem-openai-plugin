<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoriesRetrieveParams

```ts

export type MemoriesRetrieveParams = RetrieveMemoryRequest;
```

Effective request fields (including inherited fields and overrides):

- `context` (`ContextItem[] | null | undefined`, optional): Optional context items (text or binary) to provide additional context for the search.
- `fetchMemory` (`boolean | null | undefined`, optional): Whether to include streamed memory-definition records in the response. Defaults to true when omitted. These records include memory metadata and audit fields, but omit originalContent unless fetchMemoryContent is true.
- `fetchMemoryContent` (`boolean | null | undefined`, optional): Whether streamed memory-definition records include originalContent bytes. Requires fetchMemory=true. Defaults to false when omitted.
- `hnsw` (`HnswOptions | null | undefined`, optional): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve.
- `logging` (`LoggingOptions | null | undefined`, optional): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.callerAttributes to attach if caller opt-in or an admin policy logs the request.
- `message` (`string`, required): Primary query/message for semantic search.
- `outputBudget` (`TokenBudget | null | undefined`, optional): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget.
- `postProcessor` (`PostProcessor | null | undefined`, optional): Optional post-processor configuration to transform retrieval results.
- `requestedSize` (`number | null | undefined`, optional): Maximum number of memories to retrieve.
- `spaceKeys` (`SpaceKey[]`, required): List of spaces to search with optional per-embedder weight overrides.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ContextItem](ContextItem.md)
- [HnswOptions](HnswOptions.md)
- [LoggingOptions](LoggingOptions.md)
- [PostProcessor](PostProcessor.md)
- [RetrieveMemoryRequest](RetrieveMemoryRequest.md)
- [SpaceKey](SpaceKey.md)
- [TokenBudget](TokenBudget.md)
