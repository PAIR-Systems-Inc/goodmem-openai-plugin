<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Memories.CreateFromStreamAsync

Create a memory by streaming an arbitrary as the multipart file part — the .NET analog of Go's CreateFromReader, so a large upload is never fully buffered in memory. The stream is read to completion but NOT disposed (the caller owns it). Content type is inferred from when doesn't set one; the file part carries the content, so any OriginalContent/ OriginalContentB64 on the request is ignored and the caller's request is never mutated.

```csharp
Task<Memory> CreateFromStreamAsync(string spaceId, Stream content, string fileName, JsonMemoryCreationRequest? request = null, CancellationToken ct = default)
```

[Memories](../Memories.md) · [.NET](../../dotnet.md)

Related types — open only those used by your request:

- [JsonMemoryCreationRequest](../models/JsonMemoryCreationRequest.md)
