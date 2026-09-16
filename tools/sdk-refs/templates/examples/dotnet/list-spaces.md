# List spaces

```csharp
using Goodmem.Client;

var baseUrl = Environment.GetEnvironmentVariable("GOODMEM_BASE_URL")
    ?? throw new InvalidOperationException("GOODMEM_BASE_URL is required");
using var client = new GoodmemClient(new GoodmemClientOptions {
    BaseUrl = baseUrl,
    ApiKey = Environment.GetEnvironmentVariable("GOODMEM_API_KEY"),
});
await foreach (var space in client.Spaces.ListAsync())
    Console.WriteLine(space.SpaceId);
```
