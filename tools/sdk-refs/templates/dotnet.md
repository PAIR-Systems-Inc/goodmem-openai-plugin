Install `dotnet add package PairSystems.Goodmem.Client --version @VERSION@`
(.NET 8+). Construct a disposable `GoodmemClient` with `GoodmemClientOptions`
containing `BaseUrl` and `ApiKey` from environment/configuration. Request models
live in `Goodmem.Client.Models`; query options live in `Goodmem.Client.Api`.

Paginated APIs, including `ApiKeys.ListAsync`, return `IAsyncEnumerable<T>`;
`await foreach` follows cursors. Retrieval also streams via `IAsyncEnumerable`.
Methods accept `CancellationToken` for cancellation/deadlines.

Model pages show C# property names and JSON wire names. `required` requires
initialization; `?` permits null. The server can impose the documented conditional
requirements. Follow nested type links only when using those fields.

`Goodmem.Client.Errors.ApiException` carries HTTP failures with typed subclasses;
`NetworkException` represents transport failures. Preserve passages alongside
nonfatal synthesis statuses, and avoid logging raw provider errors or keys.
