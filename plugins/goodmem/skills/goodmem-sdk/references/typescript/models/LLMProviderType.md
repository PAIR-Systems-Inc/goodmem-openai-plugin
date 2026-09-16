<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMProviderType

```ts
export declare const LLMProviderType: {
    readonly OPENAI: "OPENAI";
    readonly LITELLM_PROXY: "LITELLM_PROXY";
    readonly OPEN_ROUTER: "OPEN_ROUTER";
    readonly DASHSCOPE: "DASHSCOPE";
    readonly VLLM: "VLLM";
    readonly OLLAMA: "OLLAMA";
    readonly LLAMA_CPP: "LLAMA_CPP";
    readonly CUSTOM_OPENAI_COMPATIBLE: "CUSTOM_OPENAI_COMPATIBLE";
};
export type LLMProviderType = (typeof LLMProviderType)[keyof typeof LLMProviderType];
```

[TypeScript](../../typescript.md)
