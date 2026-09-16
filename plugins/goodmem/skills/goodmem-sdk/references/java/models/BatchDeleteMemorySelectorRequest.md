<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# BatchDeleteMemorySelectorRequest

A single delete selector: either memoryId or filterSelector

- `memoryId` (`MemoryId`): Deletes one specific memory by UUID. Typed wrapper `MemoryId`; build from a raw string with `MemoryId.from(String)`.
- `filterSelector` (`FilteredDeleteMemorySelectorRequest`): Deletes a filtered set of memories within a specific space

[Java](../../java.md)

Related types — open only those used by your request:

- [FilteredDeleteMemorySelectorRequest](FilteredDeleteMemorySelectorRequest.md)
- [MemoryId](MemoryId.md)
