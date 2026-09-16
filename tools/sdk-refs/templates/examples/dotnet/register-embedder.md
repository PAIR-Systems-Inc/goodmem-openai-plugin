# Register an embedder

Register a known catalog model using an upstream provider key from the environment.
Read [create](../Embedders/CreateAsync.md) and the
[request fields](../models/EmbedderCreationRequest.md) when adapting this.
The SDK fills provider settings from its model catalog. Attach the returned embedder ID
when creating a space; registration alone does not attach it to existing spaces.

```csharp
using Goodmem.Client;
using Goodmem.Client.Models;

using var client = new GoodmemClient(new GoodmemClientOptions {
    BaseUrl = Environment.GetEnvironmentVariable("GOODMEM_BASE_URL")!,
    ApiKey = Environment.GetEnvironmentVariable("GOODMEM_API_KEY"),
});
var embedder = await client.Embedders.CreateAsync(new EmbedderCreationRequest {
    DisplayName = "Document embeddings",
    ModelIdentifier = "text-embedding-3-small",
}, apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY"));
Console.WriteLine(embedder.EmbedderId);
```
