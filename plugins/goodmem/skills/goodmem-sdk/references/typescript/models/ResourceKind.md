<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ResourceKind

```ts
export declare const ResourceKind: {
    readonly INSTANCE: "INSTANCE";
    readonly USER: "USER";
    readonly SERVICE_IDENTITY: "SERVICE_IDENTITY";
    readonly SPACE: "SPACE";
    readonly API_KEY: "API_KEY";
    readonly EMBEDDER: "EMBEDDER";
    readonly RERANKER: "RERANKER";
    readonly LLM: "LLM";
    readonly MEMORY: "MEMORY";
    readonly EXTENSION: "EXTENSION";
    readonly RETRIEVE_MEMORY_LOG_POLICY: "RETRIEVE_MEMORY_LOG_POLICY";
};
export type ResourceKind = (typeof ResourceKind)[keyof typeof ResourceKind];
```

[TypeScript](../../typescript.md)
