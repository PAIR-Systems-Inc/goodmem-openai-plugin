<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# LLMCapabilities

Capabilities and features supported by an LLM service

- `supports_chat` (`bool | None`, optional): Supports conversational/chat completion format with message roles JSON: `supportsChat`.
- `supports_completion` (`bool | None`, optional): Supports raw text completion with prompt continuation JSON: `supportsCompletion`.
- `supports_function_calling` (`bool | None`, optional): Supports function/tool calling with structured responses JSON: `supportsFunctionCalling`.
- `supports_system_messages` (`bool | None`, optional): Supports system prompts to define model behavior and context JSON: `supportsSystemMessages`.
- `supports_streaming` (`bool | None`, optional): Supports real-time token streaming during generation JSON: `supportsStreaming`.
- `supports_sampling_parameters` (`bool | None`, optional): Supports sampling parameters like temperature, top_p, and top_k for generation control JSON: `supportsSamplingParameters`.

[Python](../../python.md)
