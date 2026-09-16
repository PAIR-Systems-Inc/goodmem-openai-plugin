<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ProviderType

```ts
export declare const ProviderType: {
    readonly OPENAI: "OPENAI";
    readonly VLLM: "VLLM";
    readonly TEI: "TEI";
    readonly LLAMA_CPP: "LLAMA_CPP";
    readonly VOYAGE: "VOYAGE";
    readonly COHERE: "COHERE";
    readonly JINA: "JINA";
    readonly DASHSCOPE: "DASHSCOPE";
    readonly GEMINI: "GEMINI";
};
export type ProviderType = (typeof ProviderType)[keyof typeof ProviderType];
```

[TypeScript](../../typescript.md)
