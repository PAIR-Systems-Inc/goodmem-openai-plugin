<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Memories.CreateFromFileAsync

Create a memory from a local file via a multipart upload. The file is the content, so any OriginalContent/OriginalContentB64 on is ignored; when ContentType is unset it is inferred from the file extension. supplies optional metadata (labels, chunking, …) and is never mutated.

```csharp
Task<Memory> CreateFromFileAsync(string spaceId, string filePath, JsonMemoryCreationRequest? request = null, CancellationToken ct = default)
```

[Memories](../Memories.md) · [.NET](../../dotnet.md)

Related types — open only those used by your request:

- [JsonMemoryCreationRequest](../models/JsonMemoryCreationRequest.md)
