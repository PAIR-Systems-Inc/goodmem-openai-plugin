<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.delete

Permanently deletes a memory and its associated chunks. This operation cannot be undone and immediately removes the memory record from the database.

IDEMPOTENCY: This operation is safe to retry - may return NOT_FOUND if the memory was already deleted or never existed.

AUTHORIZATION: Requires DELETE_MEMORY on the requested memory; authority may be granted through DIRECT_MEMBERS_OF its containing space. Side effects include permanent removal of the memory record and all associated chunk data.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
