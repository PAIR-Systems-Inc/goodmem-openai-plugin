<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RetrieveMemoryRequest

Request body for semantic memory retrieval with optional embedder weight overrides.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `message` (`String`): Primary query/message for semantic search.
- `context` (`java.util.List<ContextItem>`): Optional context items (text or binary) to provide additional context for the search.
- `spaceKeys` (`java.util.List<SpaceKey>`): List of spaces to search with optional per-embedder weight overrides.
- `requestedSize` (`Integer`): Maximum number of memories to retrieve.
- `outputBudget` (`TokenBudget`): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget.
- `fetchMemory` (`Boolean`): Whether to include streamed memory-definition records in the response. Defaults to true when omitted. These records include memory metadata and audit fields, but omit originalContent unless fetchMemoryContent is true.
- `fetchMemoryContent` (`Boolean`): Whether streamed memory-definition records include originalContent bytes. Requires fetchMemory=true. Defaults to false when omitted.
- `hnsw` (`HnswOptions`): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve.
- `postProcessor` (`PostProcessor`): Optional post-processor configuration to transform retrieval results.
- `logging` (`LoggingOptions`): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.callerAttributes to attach if caller opt-in or an admin policy logs the request.

[Java](../../java.md)

Related types — open only those used by your request:

- [ContextItem](ContextItem.md)
- [HnswOptions](HnswOptions.md)
- [LoggingOptions](LoggingOptions.md)
- [PostProcessor](PostProcessor.md)
- [SpaceKey](SpaceKey.md)
- [TokenBudget](TokenBudget.md)
