<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.update

Updates an existing space with new values for the specified fields. Only name and labels can be updated. Fields not included in the request remain unchanged.

IMMUTABLE FIELDS: space_embedders, default_chunking_config, and ownerId cannot be modified after creation.

NAME UNIQUENESS: Name must be unique per owner - returns ALREADY_EXISTS if name conflicts with an existing space. Requires UPDATE_SPACE on the requested space. This operation is idempotent.

```ts
update(id: string, request: UpdateSpaceRequest, requestOptions?: RequestOptions): Promise<SpaceResponseShape>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateSpaceRequest](../models/UpdateSpaceRequest.md)
