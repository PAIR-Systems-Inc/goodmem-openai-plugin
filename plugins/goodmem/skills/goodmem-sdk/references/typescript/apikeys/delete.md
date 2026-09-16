<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# apikeys.delete

Permanently revokes an API key and immediately rejects it for future authentication. The durable credential and audit history remain stored. This operation requires DELETE_API_KEY and records the revocation time and actor; it cannot be undone. PUT /v1/apikeys/{id} with status=INACTIVE performs the same protected lifecycle transition.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[apikeys](../apikeys.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
