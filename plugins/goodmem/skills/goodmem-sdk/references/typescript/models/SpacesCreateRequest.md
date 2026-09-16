<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpacesCreateRequest

```ts

export type SpacesCreateRequest = Prettify<Omit<SpaceCreationRequest, "defaultChunkingConfig"> & {
    defaultChunkingConfig?: ChunkingConfiguration | null;
}>;
```

Effective request fields (including inherited fields and overrides):

- `defaultChunkingConfig` (`ChunkingConfiguration | null | undefined`, optional):
- `labels` (`Record<string, string> | null | undefined`, optional): A set of key-value pairs to categorize or tag the space. Used for filtering and organizational purposes.
- `name` (`string`, required): The desired name for the space. Must be unique within the user's scope.
- `ownerId` (`string | null | undefined`, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_SPACE is evaluated against the proposed space and owner.
- `spaceEmbedders` (`[SpaceEmbedderConfig, ...SpaceEmbedderConfig[]]`, required): List of embedder configurations to associate with this space. At least one embedder configuration is required. Each specifies an embedder ID and a relative default retrieval weight used when no per-request overrides are provided.
- `spaceId` (`string | null | undefined`, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [SpaceCreationRequest](SpaceCreationRequest.md)
- [SpaceEmbedderConfig](SpaceEmbedderConfig.md)
