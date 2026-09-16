<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# serviceIdentities.transferOwnership

Transfers administrative ownership to another active principal. A service identity cannot own itself. The service identity's subject, immutable creator, credentials, grants, and roles are unchanged.

```ts
transferOwnership(id: string, request: TransferOwnershipRequest, requestOptions?: RequestOptions): Promise<TransferServiceIdentityOwnershipResponseShape>
```

[serviceIdentities](../serviceIdentities.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
