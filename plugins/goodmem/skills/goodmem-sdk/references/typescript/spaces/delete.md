<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.delete

Permanently deletes a space and all associated content. This operation cannot be undone.

CASCADE DELETION: Removes the space record and cascades deletion to associated memories, chunks, and embedder associations. Requires DELETE_SPACE on the requested space. This operation is safe to retry and may return NOT_FOUND if the space was already deleted.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
