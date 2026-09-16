<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.retrieve

Retrieve Memories

Performs a streaming semantic search across one or more memory spaces and returns matching chunks ranked by relevance as well as LLM-postprocessed results (like summarization, question-answering, etc.).

Args:
    message (str): Primary query/message for semantic search.
    chronological_resort (bool, optional): Re-sort retrieved memories chronologically after semantic ranking. Defaults to true on the server. Only applies when `llm_id` or `reranker_id` is set.
    context (list[ContextItem], optional): Optional context items (text or binary) to provide additional context for the search.
    fetch_memory (bool, optional, server default=True): If `True`, memory definition events are streamed. Set to `False` to skip them.
    fetch_memory_content (bool, optional, server default=False): If `True`, includes the raw content of each memory in the response. Only applicable when `fetch_memory` is `True`.
    gen_token_budget (int, optional): Token budget for LLM post-processing. Must be positive. If the token budget is insufficient, the server will return an error. Defaults to 512 on the server. Only applies when `llm_id` is set.
    hnsw (HnswOptions, optional): Optional request-level HNSW tuning overrides. Advanced usage; available on POST retrieve.
    llm_id (str, optional): The ID of the LLM to process the retrieved memories, e.g., RAG. Assembles the nested `PostProcessor` structure automatically. If unset, no LLM will be used. Setting `llm_id` or `reranker_id` activates post-processing; the remaining post-processor params below (`llm_temp`, `gen_token_budget`, etc.) only take effect when at least one is set.
    llm_temp (float, optional): LLM temperature for post-processing. Valid range is 0.0-2.0. Defaults to 0.3 on the server. Only applies when `llm_id` is set.
    logging (LoggingOptions, optional): Optional durable request logging block for POST retrieve requests. Set logging.enabled=true to opt in, or supply flat scalar logging.caller_attributes to attach if caller opt-in or an admin policy logs the request.
    max_results (int, optional): Maximum number of retrieved memories to return. Must be positive. Defaults to 10 on the server. Only applies when `llm_id` or `reranker_id` is set.
    output_budget (TokenBudget, optional): Optional soft cap for generated retrieve replies. When set to a positive token count, chat post-processing uses this value as the LLM completion-token budget.
    post_processor (PostProcessor, optional): Optional post-processor configuration to transform retrieval results.
    prompt (str, optional): Custom prompt for LLM post-processing. If unset, the server's default prompt is used. Only applies when `llm_id` is set.
    relevance_threshold (float, optional): Minimum relevance score for retrieved memories. Only applies when `reranker_id` is set.
    requested_size (int, optional): Maximum number of memories to retrieve.
    reranker_id (str, optional): The ID of the reranker to process the retrieved memories. If unset, no reranker will be used.
    space_ids (list[str], optional): A list of space UUID strings, converted to the `space_keys` structure the API requires.
    space_keys (list[SpaceKey], optional): Full space configuration for retrieval — a list of `SpaceKey` dicts, each with a required `space_id` and optional `embedder_weights` (per-embedder weight overrides) and `filter` (metadata filter expression). Use this instead of `space_ids` when you need per-space weight tuning or filtering.
    sys_prompt (str, optional): System prompt for LLM post-processing. If unset, the server's default system prompt is used. Only applies when `llm_id` is set.
    stream (bool, optional, default=True): If True (default), return a streaming context manager; if False, collect all events into a list.

Returns:
    RetrieveMemoryStream | list[RetrieveMemoryEvent]

```python
memories.retrieve(*, message: 'str', chronological_resort: 'bool | None' = None, context: 'list[ContextItem] | None' = None, fetch_memory: 'bool | None' = None, fetch_memory_content: 'bool | None' = None, gen_token_budget: 'int | None' = None, hnsw: 'HnswOptions | None' = None, llm_id: 'str | None' = None, llm_temp: 'float | None' = None, logging: 'LoggingOptions | None' = None, max_results: 'int | None' = None, output_budget: 'TokenBudget | None' = None, post_processor: 'PostProcessor | None' = None, prompt: 'str | None' = None, relevance_threshold: 'float | None' = None, requested_size: 'int | None' = None, reranker_id: 'str | None' = None, space_ids: 'list[str] | None' = None, space_keys: 'list[SpaceKey] | None' = None, sys_prompt: 'str | None' = None, stream: 'bool' = True) -> 'RetrieveMemoryStream | list[RetrieveMemoryEvent]'
```

[memories](../memories.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [ContextItem](../models/ContextItem.md)
- [HnswOptions](../models/HnswOptions.md)
- [LoggingOptions](../models/LoggingOptions.md)
- [PostProcessor](../models/PostProcessor.md)
- [SpaceKey](../models/SpaceKey.md)
- [TokenBudget](../models/TokenBudget.md)
