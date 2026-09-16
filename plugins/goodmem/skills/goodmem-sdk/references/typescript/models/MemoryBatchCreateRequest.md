<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoryBatchCreateRequest

```ts

export type MemoryBatchCreateRequest = Prettify<{
    requests: [MemoryCreateRequest, ...MemoryCreateRequest[]];
}>;
```

Effective request fields (including inherited fields and overrides):

- `requests` (`[MemoryCreateRequest, ...MemoryCreateRequest[]]`, required):

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoryCreateRequest](MemoryCreateRequest.md)
