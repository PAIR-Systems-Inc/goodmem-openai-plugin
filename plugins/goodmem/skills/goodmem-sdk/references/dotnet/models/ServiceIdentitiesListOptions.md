<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# ServiceIdentitiesListOptions

Query options for ServiceIdentities.ListAsync. Every property is optional.

`Goodmem.Client.Api.ServiceIdentitiesListOptions`

- `IncludeDeleted` (`bool?`): Include readable permanent tombstones.
- `Label` (`IReadOnlyDictionary<string, string>?`): Filter by label key-value pairs.
- `MaxResults` (`int?`): Page size; defaults to 50 and must be between 1 and 1000.
- `NextToken` (`string?`): Opaque continuation token.
- `OwnerPrincipalId` (`string?`): Exact current administrative-owner principal UUID.

[.NET](../../dotnet.md)
