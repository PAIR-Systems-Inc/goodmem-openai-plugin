<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryCreateFromBytesRequest

```ts

export type MemoryCreateFromBytesRequest = Prettify<MemoryUploadMetadata & {
    bytes: Uint8Array | ArrayBuffer;
    contentType: string;
    filename?: string | null;
}>;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoryUploadMetadata](MemoryUploadMetadata.md)
- [Prettify](Prettify.md)
