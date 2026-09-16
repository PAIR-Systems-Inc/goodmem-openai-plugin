<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.grantsGet

Reads one live grant, or one revoked historical grant when includeRevoked is true, after requiring MANAGE_ACCESS on its policy target.

```ts
grantsGet(id: string, options?: AccessPolicyGrantsGetOptions, requestOptions?: RequestOptions): Promise<AuthorizationGrantResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AccessPolicyGrantsGetOptions](../models/AccessPolicyGrantsGetOptions.md)
- [RequestOptions](../models/RequestOptions.md)
