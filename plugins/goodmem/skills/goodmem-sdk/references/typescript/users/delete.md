<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.delete

Permanently soft-deletes the user and invalidates credentials acting for that subject. The GoodMem instance owner cannot be deleted; transfer ownership first. Repeating an authorized delete succeeds without rewriting audit data.

```ts
delete(id: string, requestOptions?: RequestOptions): Promise<void>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
