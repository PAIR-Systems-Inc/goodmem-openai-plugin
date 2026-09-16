<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# CreateAuthorizationGrantRequest

Creates one live direct authorization grant.

- `grantId` (`string | null`, optional): Optional caller-provided grant UUID.
- `audience` (`GrantAudience`, required): Audience receiving the grant.
- `rule` (`AccessPolicyRule`, required): Authorization descriptor to grant.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AccessPolicyRule](AccessPolicyRule.md)
- [GrantAudience](GrantAudience.md)
