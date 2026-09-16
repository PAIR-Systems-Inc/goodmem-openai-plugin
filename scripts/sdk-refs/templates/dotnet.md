# GoodMem .NET SDK

Install `dotnet add package PairSystems.Goodmem.Client --version @VERSION@`
(.NET 8+). The client is asynchronous and disposable; request models live in
`Goodmem.Client.Models`, options in `Goodmem.Client.Api`.

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

Paginated APIs, including `ApiKeys.ListAsync`, return `IAsyncEnumerable<T>`;
`await foreach` follows cursors. Retrieval also streams via `IAsyncEnumerable`.
Methods accept `CancellationToken` for deadlines/cancellation. After creation,
poll `Memories.GetAsync` with a deadline, stop on FAILED, and retrieve only after
COMPLETED. See the Python example in [the SDK skill](../SKILL.md) for the flow.

`Goodmem.Client.Errors.ApiException` carries HTTP failures and typed subclasses;
`NetworkException` represents transport failures. Avoid logging raw provider
error bodies or keys. Space access uses policies; no public-read creation flag.
