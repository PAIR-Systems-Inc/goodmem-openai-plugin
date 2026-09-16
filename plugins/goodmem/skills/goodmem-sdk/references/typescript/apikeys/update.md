<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# apikeys.update

Updates an existing API key's labels or lifecycle status. Key ID, subject, ownership, key material, validity window, and creation audit fields remain immutable. Label changes require UPDATE_API_KEY; setting status=INACTIVE permanently revokes the key and requires DELETE_API_KEY; a request doing both requires both operations. Revoked keys cannot be reactivated. Side effects include updating administrative audit fields and, for revocation, recording the revocation time and actor.

```ts
update(id: string, request: UpdateApiKeyRequest, requestOptions?: RequestOptions): Promise<ApiKeyResponseShape>
```

[apikeys](../apikeys.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateApiKeyRequest](../models/UpdateApiKeyRequest.md)
