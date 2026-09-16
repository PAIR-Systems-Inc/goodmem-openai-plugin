<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# GrantAudience

Exactly one principal or the all-authenticated audience.

```ts

export type GrantAudience = RequireExactlyOne<GrantAudienceBase, "allAuthenticated" | "principalId">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [GrantAudienceBase](GrantAudienceBase.md)
- [RequireExactlyOne](RequireExactlyOne.md)
