<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.grantsDelete

Soft-revokes one grant and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS on the target.

```ts
grantsDelete(id: string, requestOptions?: RequestOptions): Promise<AuthorizationGrantResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
