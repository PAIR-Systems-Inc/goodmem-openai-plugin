<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# embedders.delete

Permanently deletes an embedder configuration. This operation cannot be undone and removes the embedder record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete embeddings previously created with this embedder - existing embeddings remain accessible.

CONFLICT: Returns HTTP 409 Conflict if the embedder is still referenced by a space. Requires DELETE_EMBEDDER on the requested embedder.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[embedders](../embedders.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
