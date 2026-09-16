<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# GrantAudience

Exactly one principal or the all-authenticated audience.

- `principalId` (`PrincipalId`): Active HUMAN or SERVICE principal UUID. Typed wrapper `PrincipalId`; build from a raw string with `PrincipalId.from(String)`.
- `allAuthenticated` (`GrantAudienceAllAuthenticated`): Set to true to address every authenticated principal.

[Java](../../java.md)

Related types — open only those used by your request:

- [GrantAudienceAllAuthenticated](GrantAudienceAllAuthenticated.md)
- [PrincipalId](PrincipalId.md)
