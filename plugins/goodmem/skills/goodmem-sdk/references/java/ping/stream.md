<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ping.stream

Stream ping probe results

Opens a streaming ping session and returns per-probe results plus a terminal summary. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

```java
PingStream stream(PingStreamRequest request)
```

[ping](../ping.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [PingStreamRequest](../models/PingStreamRequest.md)
