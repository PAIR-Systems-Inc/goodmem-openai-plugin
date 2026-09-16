<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AccessPolicyRoleAssignmentsListOptions

Query options for AccessPolicy.RoleAssignmentsListAsync. Every property is optional.

`Goodmem.Client.Api.AccessPolicyRoleAssignmentsListOptions`

- `IncludeRevoked` (`bool?`): Include revoked history.
- `MaxResults` (`int?`): Page size; 0 or omission uses the default of 50, maximum 1,000.
- `NextToken` (`string?`): Opaque continuation token.
- `ResourceId` (`string?`): Required space UUID; omitted for INSTANCE.
- `ResourceKind` (`string?`): Required INSTANCE or SPACE kind.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ResourceKind](ResourceKind.md)
