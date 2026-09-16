<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.grantsList

Lists grants attached to one resource. MANAGE_ACCESS is required on that resource; continuation tokens are bound to the caller and filters.

```ts
grantsList(options?: AccessPolicyGrantsListOptions, requestOptions?: RequestOptions): Promise<Page<AuthorizationGrantResponseShape>>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AccessPolicyGrantsListOptions](../models/AccessPolicyGrantsListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
