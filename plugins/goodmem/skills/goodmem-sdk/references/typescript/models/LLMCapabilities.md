<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMCapabilities

Capabilities and features supported by an LLM service

- `supportsChat` (`boolean | null`, optional): Supports conversational/chat completion format with message roles
- `supportsCompletion` (`boolean | null`, optional): Supports raw text completion with prompt continuation
- `supportsFunctionCalling` (`boolean | null`, optional): Supports function/tool calling with structured responses
- `supportsSystemMessages` (`boolean | null`, optional): Supports system prompts to define model behavior and context
- `supportsStreaming` (`boolean | null`, optional): Supports real-time token streaming during generation
- `supportsSamplingParameters` (`boolean | null`, optional): Supports sampling parameters like temperature, top_p, and top_k for generation control

[TypeScript](../../typescript.md)
