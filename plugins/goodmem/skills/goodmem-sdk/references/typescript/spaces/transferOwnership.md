<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.transferOwnership

Transfers an existing space to another active human or service principal. The current space owner, the GoodMem instance owner, or an instance administrator may transfer it; a space-scoped administrator cannot. Only owner and update-audit fields change. Memories, embedder associations, grants, and role assignments remain unchanged. This operation is not idempotent under response semantics: after an unknown outcome, read the space before retrying.

```ts
transferOwnership(id: string, request: TransferOwnershipRequest, requestOptions?: RequestOptions): Promise<TransferSpaceOwnershipResponseShape>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
