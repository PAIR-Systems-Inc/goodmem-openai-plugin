<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ping.once

Runs a single ping probe and returns the probe result. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

```ts
once(request: PingOnceRequest, requestOptions?: RequestOptions): Promise<PingResultResponseShape>
```

[ping](../ping.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [PingOnceRequest](../models/PingOnceRequest.md)
- [RequestOptions](../models/RequestOptions.md)
