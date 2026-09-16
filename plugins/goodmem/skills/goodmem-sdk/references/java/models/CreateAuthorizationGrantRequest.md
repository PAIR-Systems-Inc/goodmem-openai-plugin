<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# CreateAuthorizationGrantRequest

Creates one live direct authorization grant.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `grantId` (`GrantId`): Optional caller-provided grant UUID. Typed wrapper `GrantId`; build from a raw string with `GrantId.from(String)`.
- `audience` (`GrantAudience`): Audience receiving the grant.
- `rule` (`AccessPolicyRule`): Authorization descriptor to grant.

[Java](../../java.md)

Related types — open only those used by your request:

- [AccessPolicyRule](AccessPolicyRule.md)
- [GrantAudience](GrantAudience.md)
- [GrantId](GrantId.md)
