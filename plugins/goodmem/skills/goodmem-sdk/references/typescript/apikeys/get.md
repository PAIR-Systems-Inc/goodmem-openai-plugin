<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# apikeys.get

Returns complete non-secret metadata for one existing credential after requiring effective READ_API_KEY authority. The immutable ceiling is always complete and ceilingOmitted is false. Raw key material and hashes are never returned.

```ts
get(id: string, requestOptions?: RequestOptions): Promise<ApiKeyResponseShape>
```

[apikeys](../apikeys.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
