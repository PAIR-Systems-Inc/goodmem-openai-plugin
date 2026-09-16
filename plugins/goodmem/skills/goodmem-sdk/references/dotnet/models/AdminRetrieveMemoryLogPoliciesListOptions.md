<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AdminRetrieveMemoryLogPoliciesListOptions

Query options for Admin.RetrieveMemoryLogPoliciesListAsync. Every property is optional.

`Goodmem.Client.Api.AdminRetrieveMemoryLogPoliciesListOptions`

- `ActiveAt` (`long?`): Only return policies active at this millisecond epoch timestamp.
- `IncludeDeleted` (`bool?`): Whether to include tombstoned policies.
- `Label` (`IReadOnlyDictionary<string, string>?`): Filter by label key-value pairs.
- `MaxResults` (`int?`): Maximum number of policies to return.
- `NameFilter` (`string?`): Case-insensitive substring filter on policy display names.
- `NextToken` (`string?`): Opaque pagination token returned by the previous list response.
- `SortBy` (`string?`): Sort field: created_at, updated_at, or display_name.
- `SortOrder` (`SortOrder?`): Sort order.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
