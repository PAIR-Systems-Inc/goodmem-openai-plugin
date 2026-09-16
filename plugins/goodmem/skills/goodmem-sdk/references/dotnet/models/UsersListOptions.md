<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UsersListOptions

Query options for Users.ListAsync. Every property is optional.

`Goodmem.Client.Api.UsersListOptions`

- `IncludeDeleted` (`bool?`): Include readable permanent tombstones.
- `IncludeEnrollmentSummary` (`bool?`): Request non-secret enrollment posture on active rows where the caller also has MANAGE_USER_ENROLLMENT.
- `Label` (`IReadOnlyDictionary<string, string>?`): Filter by label key-value pairs.
- `MaxResults` (`int?`): Page size; defaults to 50 and must be between 1 and 1000.
- `NextToken` (`string?`): Opaque continuation token.

[.NET](../../dotnet.md)
