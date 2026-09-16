<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.create

Creates a new space with the provided name, labels, and embedder configuration. A space is a container for organizing related memories.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_SPACE is evaluated against the proposed space and owner.

EMBEDDER REQUIREMENTS: At least one embedder configuration must be specified. Every referenced embedder must exist, and the caller must have EXECUTE_EMBEDDER on each one.

DUPLICATE DETECTION: Returns ALREADY_EXISTS if another space exists with identical {ownerId, name} (case-sensitive). This operation is NOT idempotent.

```ts
create(request: SpacesCreateRequest, requestOptions?: RequestOptions): Promise<SpaceResponseShape>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [SpacesCreateRequest](../models/SpacesCreateRequest.md)
