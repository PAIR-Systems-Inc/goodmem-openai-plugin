<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# MemoriesListOptions

Query options for Memories.ListAsync. Every property is optional.

`Goodmem.Client.Api.MemoriesListOptions`

- `Filter` (`string?`): Optional metadata filter expression for list results.
- `IncludeContent` (`bool?`): Whether to include the original content in the response (defaults to false).
- `IncludeProcessingHistory` (`bool?`): Whether to include background job processing history in the response (defaults to false).
- `MaxResults` (`int?`): Maximum number of results per page (defaults to 50, clamped to [1, 500]).
- `NextToken` (`string?`): Opaque pagination token for the next page.
- `SortBy` (`string?`): Field to sort by (e.g., 'created_at').
- `SortOrder` (`SortOrder?`): Sort direction (ASCENDING or DESCENDING).
- `StatusFilter` (`string?`): Filter memories by processing status (PENDING, PROCESSING, COMPLETED, FAILED).

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
