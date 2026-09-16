<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RetrieveMemoryRequest

Request body for semantic memory retrieval with optional embedder weight overrides.

`Goodmem.Client.Models.RetrieveMemoryRequest`

- `Context` (`IReadOnlyList<ContextItem>?`): Optional context items (text or binary) to provide additional context for the search. JSON: `context`.
- `FetchMemory` (`bool?`): Whether to include streamed memory-definition records in the response. Defaults to true when omitted. These records include memory metadata and audit fields, but omit originalContent unless fetchMemoryContent is true. JSON: `fetchMemory`.
- `FetchMemoryContent` (`bool?`): Whether streamed memory-definition records include originalContent bytes. Requires fetchMemory=true. Defaults to false when omitted. JSON: `fetchMemoryContent`.
- `Hnsw` (`HnswOptions?`): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve. JSON: `hnsw`.
- `Logging` (`LoggingOptions?`): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.callerAttributes to attach if caller opt-in or an admin policy logs the request. JSON: `logging`.
- `Message` (`string`, required): Primary query/message for semantic search. JSON: `message`.
- `OutputBudget` (`TokenBudget?`): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget. JSON: `outputBudget`.
- `PostProcessor` (`PostProcessor?`): Optional post-processor configuration to transform retrieval results. JSON: `postProcessor`.
- `RequestedSize` (`int?`): Maximum number of memories to retrieve. JSON: `requestedSize`.
- `SpaceKeys` (`IReadOnlyList<SpaceKey>?`): List of spaces to search with optional per-embedder weight overrides. JSON: `spaceKeys`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ContextItem](ContextItem.md)
- [HnswOptions](HnswOptions.md)
- [LoggingOptions](LoggingOptions.md)
- [PostProcessor](PostProcessor.md)
- [SpaceKey](SpaceKey.md)
- [TokenBudget](TokenBudget.md)
