<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# serviceIdentities.update

Updates only fields present in the request. Empty description clears that optional field. Ownership changes use the dedicated transfer endpoint.

```ts
update(id: string, request: UpdateServiceIdentityRequest, requestOptions?: RequestOptions): Promise<ServiceIdentityResponseShape>
```

[serviceIdentities](../serviceIdentities.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateServiceIdentityRequest](../models/UpdateServiceIdentityRequest.md)
