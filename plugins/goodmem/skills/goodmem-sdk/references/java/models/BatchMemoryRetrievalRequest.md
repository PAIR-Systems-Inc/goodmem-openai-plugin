<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# BatchMemoryRetrievalRequest

Request body for retrieving multiple memories by their IDs

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `memoryIds` (`java.util.List<MemoryId>`): Array of memory IDs to retrieve. Element type `MemoryId`; build each entry from a raw string with `MemoryId.from(String)`.
- `includeContent` (`Boolean`): Whether to include the original content in the response
- `includeProcessingHistory` (`Boolean`): Whether to include background job processing history for each memory

[Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](MemoryId.md)
