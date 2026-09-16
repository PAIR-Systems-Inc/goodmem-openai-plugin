<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RetrieveMemoryRequest

Request body for semantic memory retrieval with optional embedder weight overrides.

- `message` (`string`, required): Primary query/message for semantic search.
- `context` (`Array<ContextItem> | null`, optional): Optional context items (text or binary) to provide additional context for the search.
- `spaceKeys` (`Array<SpaceKey>`, required): List of spaces to search with optional per-embedder weight overrides.
- `requestedSize` (`number | null`, optional): Maximum number of memories to retrieve.
- `outputBudget` (`TokenBudget | null`, optional): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget.
- `fetchMemory` (`boolean | null`, optional): Whether to include streamed memory-definition records in the response. Defaults to true when omitted. These records include memory metadata and audit fields, but omit originalContent unless fetchMemoryContent is true.
- `fetchMemoryContent` (`boolean | null`, optional): Whether streamed memory-definition records include originalContent bytes. Requires fetchMemory=true. Defaults to false when omitted.
- `hnsw` (`HnswOptions | null`, optional): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve.
- `postProcessor` (`PostProcessor | null`, optional): Optional post-processor configuration to transform retrieval results.
- `logging` (`LoggingOptions | null`, optional): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.callerAttributes to attach if caller opt-in or an admin policy logs the request.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ContextItem](ContextItem.md)
- [HnswOptions](HnswOptions.md)
- [LoggingOptions](LoggingOptions.md)
- [PostProcessor](PostProcessor.md)
- [SpaceKey](SpaceKey.md)
- [TokenBudget](TokenBudget.md)
