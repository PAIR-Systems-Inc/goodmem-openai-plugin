<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# serviceIdentities.get

Returns a service identity after applying READ_SERVICE_IDENTITY authority. includeDeleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority.

```ts
get(id: string, options?: ServiceIdentitiesGetOptions, requestOptions?: RequestOptions): Promise<ServiceIdentityResponseShape>
```

[serviceIdentities](../serviceIdentities.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [ServiceIdentitiesGetOptions](../models/ServiceIdentitiesGetOptions.md)
