<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# admin.transferInstanceOwnership

Transfers the singleton GoodMem instance to another active human principal. Only the current instance owner may invoke this operation; ADMIN, MANAGE_ACCESS, and ordinary grants are insufficient. Ownership and the synthetic ROOT assignment move atomically. All ordinary roles, including ADMIN, remain unchanged. No credential is created or returned. After an unknown outcome, read the current owner before retrying.

```ts
transferInstanceOwnership(request: TransferOwnershipRequest, requestOptions?: RequestOptions): Promise<TransferInstanceOwnershipResponseShape>
```

[admin](../admin.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
