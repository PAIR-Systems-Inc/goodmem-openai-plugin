<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# serviceIdentities.delete

Permanently soft-deletes the principal. Its stored credentials remain audit records but can no longer authenticate because their subject is deleted. Repeating an authorized delete succeeds without rewriting audit data.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[serviceIdentities](../serviceIdentities.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
