<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# BatchDeleteMemorySelectorRequest

A single delete selector: either memoryId or filterSelector

`Goodmem.Client.Models.BatchDeleteMemorySelectorRequest`

- `FilterSelector` (`FilteredDeleteMemorySelectorRequest?`): Deletes a filtered set of memories within a specific space JSON: `filterSelector`.
- `MemoryId` (`string?`): Deletes one specific memory by UUID JSON: `memoryId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [FilteredDeleteMemorySelectorRequest](FilteredDeleteMemorySelectorRequest.md)
