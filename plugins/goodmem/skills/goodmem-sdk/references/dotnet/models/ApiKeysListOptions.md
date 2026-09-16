<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# ApiKeysListOptions

Query options for ApiKeys.ListAsync. Every property is optional.

`Goodmem.Client.Api.ApiKeysListOptions`

- `LifecycleState` (`string?`): Filter by precise lifecycle state.
- `MaxResults` (`int?`): Page size; FULL defaults to 10 and permits at most 20, while BASIC defaults to 50 and permits at most 1,000.
- `NextToken` (`string?`): Opaque continuation token returned by the preceding page.
- `OwnerPrincipalId` (`string?`): Filter by exact administrative-owner UUID.
- `SubjectPrincipalId` (`string?`): Filter by exact subject-principal UUID.
- `View` (`string?`): Metadata projection; omission defaults to FULL.

[.NET](../../dotnet.md)
