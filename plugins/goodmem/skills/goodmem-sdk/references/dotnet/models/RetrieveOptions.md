<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RetrieveOptions

Flat convenience parameters for Memories.RetrieveAsync. SpaceIds is expanded into SpaceKeys and the flat ChatPostProcessor keys are assembled into a PostProcessor; every property is optional. For full control over the request body use Memories.RetrieveRawAsync.

`Goodmem.Client.Api.RetrieveOptions`

- `ChronologicalResort` (`bool?`): Re-sort retrieved memories chronologically after semantic ranking. Defaults to true on the server. Only applies when `llm_id` or `reranker_id` is set. Requires at least one of llm_id or reranker_id to be set — RetrieveAsync rejects it otherwise.
- `FetchMemory` (`bool?`): Whether memory-definition records are streamed (server default true).
- `FetchMemoryContent` (`bool?`): Whether streamed memory records include original content bytes.
- `GenTokenBudget` (`int?`): Token budget for LLM post-processing. Must be positive. If the token budget is insufficient, the server will return an error. Defaults to 512 on the server. Only applies when `llm_id` is set. Requires llm_id to be set — RetrieveAsync rejects it otherwise.
- `LlmId` (`string?`): The ID of the LLM to process the retrieved memories, e.g., RAG. Assembles the nested `PostProcessor` structure automatically. If unset, no LLM will be used. Setting `llm_id` or `reranker_id` activates post-processing; the remaining post-processor params below (`llm_temp`, `gen_token_budget`, etc.) only take effect when at least one is set. Activates LLM post-processing and unlocks the llmTemp / genTokenBudget / prompt / sysPrompt keys.
- `LlmTemp` (`double?`): LLM temperature for post-processing. Valid range is 0.0-2.0. Defaults to 0.3 on the server. Only applies when `llm_id` is set. Requires llm_id to be set — RetrieveAsync rejects it otherwise.
- `MaxResults` (`int?`): Maximum number of retrieved memories to return. Must be positive. Defaults to 10 on the server. Only applies when `llm_id` or `reranker_id` is set. Requires at least one of llm_id or reranker_id to be set — RetrieveAsync rejects it otherwise.
- `Prompt` (`string?`): Custom prompt for LLM post-processing. If unset, the server's default prompt is used. Only applies when `llm_id` is set. Requires llm_id to be set — RetrieveAsync rejects it otherwise.
- `RelevanceThreshold` (`double?`): Minimum relevance score for retrieved memories. Only applies when `reranker_id` is set. Requires reranker_id to be set — RetrieveAsync rejects it otherwise.
- `RequestedSize` (`int?`): Maximum number of memories to retrieve.
- `RerankerId` (`string?`): The ID of the reranker to process the retrieved memories. If unset, no reranker will be used. Activates reranking and unlocks relevanceThreshold.
- `SpaceIds` (`IReadOnlyList<string>?`): Space UUIDs to search; each is expanded into a SpaceKey.
- `SysPrompt` (`string?`): System prompt for LLM post-processing. If unset, the server's default system prompt is used. Only applies when `llm_id` is set. Requires llm_id to be set — RetrieveAsync rejects it otherwise.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [PostProcessor](PostProcessor.md)
- [SpaceKey](SpaceKey.md)
