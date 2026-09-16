<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.batchDelete

Delete memories in batch

Deletes memories using selector entries. Each selector can target either a specific memory ID or a filtered subset scoped to a specific space. Each selected memory requires DELETE_MEMORY; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```java
BatchMemoryResponse batchDelete(BatchMemoryDeletionRequest request)
```

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [BatchMemoryDeletionRequest](../models/BatchMemoryDeletionRequest.md)
