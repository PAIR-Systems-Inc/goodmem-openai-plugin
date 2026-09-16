<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ApiKeyAuth

Configuration for classic API-key authentication.

```ts

export type ApiKeyAuth = RequireExactlyOne<ApiKeyAuthBase, "inlineSecret" | "secretRef">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ApiKeyAuthBase](ApiKeyAuthBase.md)
- [RequireExactlyOne](RequireExactlyOne.md)
