<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpacesCreateRequest

```ts

export type SpacesCreateRequest = Prettify<Omit<SpaceCreationRequest, "defaultChunkingConfig"> & {
    defaultChunkingConfig?: ChunkingConfiguration | null;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ChunkingConfiguration](ChunkingConfiguration.md)
- [Prettify](Prettify.md)
- [SpaceCreationRequest](SpaceCreationRequest.md)
