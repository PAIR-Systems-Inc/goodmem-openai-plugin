<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Ingest and retrieve

Use an existing space with an embedder. Read [create](../Memories/CreateAsync.md),
[get](../Memories/GetAsync.md), and [retrieve](../Memories/RetrieveAsync.md) when adapting this.
Request details: [memory body](../models/JsonMemoryCreationRequest.md) and
[retrieval options](../models/RetrieveOptions.md).

```csharp
using Goodmem.Client;
using Goodmem.Client.Api;
using Goodmem.Client.Models;

using var client = new GoodmemClient(new GoodmemClientOptions {
    BaseUrl = Environment.GetEnvironmentVariable("GOODMEM_BASE_URL")!,
    ApiKey = Environment.GetEnvironmentVariable("GOODMEM_API_KEY"),
});
var spaceId = Environment.GetEnvironmentVariable("GOODMEM_SPACE_ID")!;
var memory = await client.Memories.CreateAsync(new JsonMemoryCreationRequest {
    SpaceId = spaceId,
    OriginalContent = "GoodMem stores and retrieves memories.",
    ContentType = "text/plain",
});
using var deadline = new CancellationTokenSource(TimeSpan.FromMinutes(2));
while (memory.ProcessingStatus != "COMPLETED") {
    if (memory.ProcessingStatus == "FAILED")
        throw new InvalidOperationException("Memory processing failed; inspect job history in GoodMem.");
    await Task.Delay(500, deadline.Token);
    memory = await client.Memories.GetAsync(memory.MemoryId, ct: deadline.Token);
}
await foreach (var item in client.Memories.RetrieveAsync(
    "what does GoodMem do?", new RetrieveOptions { SpaceIds = new[] { spaceId } }, deadline.Token)) {
    if (item.RetrievedItem?.Chunk is { } chunk)
        Console.WriteLine(chunk.Chunk.ChunkText);
}
```

[.NET](../../dotnet.md)
