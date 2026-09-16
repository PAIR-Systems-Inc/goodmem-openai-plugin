<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Memories.RetrieveAsync

Runs a retrieval from the flat convenience parameters: SpaceIds expand into SpaceKeys and the flat post-processor keys assemble into a ChatPostProcessor.

```csharp
IAsyncEnumerable<RetrieveMemoryEvent> RetrieveAsync(string message, RetrieveOptions? options = null, CancellationToken ct = default)
```

[Memories](../Memories.md) · [.NET](../../dotnet.md)

Related types — open only those used by your request:

- [RetrieveOptions](../models/RetrieveOptions.md)
