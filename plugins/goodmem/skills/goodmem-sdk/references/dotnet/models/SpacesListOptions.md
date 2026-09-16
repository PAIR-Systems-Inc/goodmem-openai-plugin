<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# SpacesListOptions

Query options for Spaces.ListAsync. Every property is optional.

`Goodmem.Client.Api.SpacesListOptions`

- `Label` (`IReadOnlyDictionary<string, string>?`): Filter by label key-value pairs.
- `MaxResults` (`int?`): Maximum number of results to return in a single page (defaults to 50, clamped to [1, 1000]).
- `NameFilter` (`string?`): Filter spaces by name using glob pattern matching.
- `NextToken` (`string?`): Pagination token for retrieving the next set of results.
- `OwnerId` (`string?`): Filter the already-authorized result set by owner principal UUID.
- `SortBy` (`string?`): Field to sort by: 'created_time', 'updated_time', or 'name' (default: 'created_time').
- `SortOrder` (`SortOrder?`): Sort order (ASCENDING or DESCENDING, default: DESCENDING).

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
