<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ping.stream

Opens a streaming ping session and returns per-probe results plus a terminal summary. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

```ts
stream(request: PingStreamParams, requestOptions?: RequestOptions): AsyncIterable<PingEventResponseShape>
```

[ping](../ping.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [PingStreamParams](../models/PingStreamParams.md)
- [RequestOptions](../models/RequestOptions.md)
