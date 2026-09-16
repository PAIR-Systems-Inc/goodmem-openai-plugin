<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ping.once

Run a single ping probe

Runs a single ping probe and returns the probe result. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

```java
PingResult once(PingOnceRequest request)
```

[ping](../ping.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [PingOnceRequest](../models/PingOnceRequest.md)
