<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# LlmCapabilities

Capabilities and features supported by an LLM service

`Goodmem.Client.Models.LlmCapabilities`

- `SupportsChat` (`bool?`): Supports conversational/chat completion format with message roles JSON: `supportsChat`.
- `SupportsCompletion` (`bool?`): Supports raw text completion with prompt continuation JSON: `supportsCompletion`.
- `SupportsFunctionCalling` (`bool?`): Supports function/tool calling with structured responses JSON: `supportsFunctionCalling`.
- `SupportsSamplingParameters` (`bool?`): Supports sampling parameters like temperature, top_p, and top_k for generation control JSON: `supportsSamplingParameters`.
- `SupportsStreaming` (`bool?`): Supports real-time token streaming during generation JSON: `supportsStreaming`.
- `SupportsSystemMessages` (`bool?`): Supports system prompts to define model behavior and context JSON: `supportsSystemMessages`.

[.NET](../../dotnet.md)
