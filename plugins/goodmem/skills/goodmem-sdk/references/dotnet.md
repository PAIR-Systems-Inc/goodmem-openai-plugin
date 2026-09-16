<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# GoodMem .NET SDK

[Published package 2.0.2](https://www.nuget.org/packages/PairSystems.Goodmem.Client/2.0.2); server guidance assumes GoodMem 1.0.320 or later.

Install `dotnet add package PairSystems.Goodmem.Client --version 2.0.2`
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

## Examples

- [Ingest retrieve](dotnet/examples/ingest-retrieve.md)
- [Issue scoped key](dotnet/examples/issue-scoped-key.md)
- [List spaces](dotnet/examples/list-spaces.md)
- [Register embedder](dotnet/examples/register-embedder.md)

## Namespaces

Open one index, then the needed operation and models. Search for a symbol inside this language directory when search is available; avoid reading whole directories.

- [AccessPolicy](dotnet/AccessPolicy.md)
- [Admin](dotnet/Admin.md)
- [ApiKeys](dotnet/ApiKeys.md)
- [Embedders](dotnet/Embedders.md)
- [Instance](dotnet/Instance.md)
- [Llms](dotnet/Llms.md)
- [Memories](dotnet/Memories.md)
- [Ocr](dotnet/Ocr.md)
- [Ping](dotnet/Ping.md)
- [Rerankers](dotnet/Rerankers.md)
- [ServiceIdentities](dotnet/ServiceIdentities.md)
- [Spaces](dotnet/Spaces.md)
- [System](dotnet/System.md)
- [UserEnrollments](dotnet/UserEnrollments.md)
- [Users](dotnet/Users.md)

[SDK rules](../SKILL.md)
