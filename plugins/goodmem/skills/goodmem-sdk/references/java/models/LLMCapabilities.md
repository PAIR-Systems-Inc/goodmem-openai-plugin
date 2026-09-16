<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LLMCapabilities

Capabilities and features supported by an LLM service

- `supportsChat` (`Boolean`): Supports conversational/chat completion format with message roles
- `supportsCompletion` (`Boolean`): Supports raw text completion with prompt continuation
- `supportsFunctionCalling` (`Boolean`): Supports function/tool calling with structured responses
- `supportsSystemMessages` (`Boolean`): Supports system prompts to define model behavior and context
- `supportsStreaming` (`Boolean`): Supports real-time token streaming during generation
- `supportsSamplingParameters` (`Boolean`): Supports sampling parameters like temperature, top_p, and top_k for generation control

[Java](../../java.md)
