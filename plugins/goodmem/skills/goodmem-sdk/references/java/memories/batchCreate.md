<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.batchCreate

Create multiple memories in a batch

Creates multiple memories in a single operation, with individual success/failure results. Each item requires CREATE_MEMORY on its containing space; authorization failures are reported in the corresponding item result.

```java
BatchMemoryResponse batchCreate(JsonBatchMemoryCreationRequest request)
```

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [JsonBatchMemoryCreationRequest](../models/JsonBatchMemoryCreationRequest.md)
