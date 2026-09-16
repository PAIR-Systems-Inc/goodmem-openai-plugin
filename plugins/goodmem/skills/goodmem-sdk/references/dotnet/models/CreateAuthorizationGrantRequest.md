<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# CreateAuthorizationGrantRequest

Creates one live direct authorization grant.

`Goodmem.Client.Models.CreateAuthorizationGrantRequest`

- `Audience` (`GrantAudience`, required): Audience receiving the grant. JSON: `audience`.
- `GrantId` (`string?`): Optional caller-provided grant UUID. JSON: `grantId`.
- `Rule` (`AccessPolicyRule`, required): Authorization descriptor to grant. JSON: `rule`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [AccessPolicyRule](AccessPolicyRule.md)
- [GrantAudience](GrantAudience.md)
