<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.batchGet

Get multiple memories by ID

Retrieves multiple memories in a single operation, with individual success/failure results. Each item requires READ_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```java
BatchMemoryResponse batchGet(BatchMemoryRetrievalRequest request)
```

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [BatchMemoryRetrievalRequest](../models/BatchMemoryRetrievalRequest.md)
