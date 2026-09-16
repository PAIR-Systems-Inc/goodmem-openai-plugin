<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# apikeys.list

Requires LIST_API_KEY on the singleton instance, then retrieves one UUID-ordered page containing only credentials that independently pass READ_API_KEY. Both gates use the authenticated principal's live authority and any scoped-key ceiling. Subject, owner, and lifecycle filters are applied after authorization. FULL includes complete immutable ceilings; BASIC omits them, sets ceilingOmitted=true, and permits larger pages. Raw key values and key hashes are never returned.

```ts
list(options?: ApikeysListOptions, requestOptions?: RequestOptions): Promise<Page<ApiKeyResponseShape>>
```

[apikeys](../apikeys.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ApikeysListOptions](../models/ApikeysListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
