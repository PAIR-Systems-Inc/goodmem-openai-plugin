<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AccessPolicyGrantsListOptions

Query options for AccessPolicy.GrantsListAsync. Every property is optional.

`Goodmem.Client.Api.AccessPolicyGrantsListOptions`

- `IncludeRevoked` (`bool?`): Include revoked history.
- `MaxResults` (`int?`): Page size; 0 or omission uses the default of 50, maximum 1,000.
- `NextToken` (`string?`): Opaque continuation token.
- `ResourceId` (`string?`): Required target UUID except when resourceKind is INSTANCE.
- `ResourceKind` (`string?`): Required target resource kind.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ResourceKind](ResourceKind.md)
