<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# BatchMemoryRetrievalRequest

Request body for retrieving multiple memories by their IDs

`Goodmem.Client.Models.BatchMemoryRetrievalRequest`

- `IncludeContent` (`bool?`): Whether to include the original content in the response JSON: `includeContent`.
- `IncludeProcessingHistory` (`bool?`): Whether to include background job processing history for each memory JSON: `includeProcessingHistory`.
- `MemoryIds` (`IReadOnlyList<string>`, required): Array of memory IDs to retrieve JSON: `memoryIds`.

[.NET](../../dotnet.md)
