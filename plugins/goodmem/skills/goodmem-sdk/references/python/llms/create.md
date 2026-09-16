<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# llms.create

Create a new LLM

Creates a new LLM configuration for text generation services. LLMs represent connections to different language model API services (like OpenAI, vLLM, etc.) and include all the necessary configuration to use them for text generation.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another LLM exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison. The api_path field defaults to '/chat/completions' if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless owner_id is provided; CREATE_LLM is evaluated against the proposed LLM and owner.

Args:
    display_name (str): User-facing name of the LLM
    model_identifier (str): When a known model, auto-fills `provider_type`, `endpoint_url`, `max_context_length`, and `supported_modalities`.
    api_key (str, optional): Converts a plain API key string to the full `EndpointAuthentication` structure (i.e. `{"kind": "CREDENTIAL_KIND_API_KEY", "api_key": {"inline_secret": "sk-..."}}`).
    api_path (str, optional, server default='/chat/completions'): API path for chat/completions request (defaults to `/chat/completions` if not provided).
    capabilities (LLMCapabilities, optional): LLM capabilities defining supported features and modes. Optional — server infers capabilities from model identifier if not provided.
    client_config (dict[str, Any], optional): Provider-specific client configuration as flexible JSON structure
    credentials (EndpointAuthentication, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
    dashscope_api_dialect (DashScopeApiDialect, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. When omitted, a recognized api_path determines the dialect; otherwise OPENAI_COMPATIBLE is used.
    default_sampling_params (LLMSamplingParams, optional): Default sampling parameters for generation requests
    description (str, optional): Description of the LLM
    endpoint_url (str, optional): Base URL for the LLM endpoint (OpenAI-compatible base, typically ends with `/v1`). Auto-inferred from `provider_type` for known providers; required when `model_identifier` is not in the registry.
    labels (dict[str, str], optional): User-defined labels for categorization
    llm_id (str, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
    max_context_length (int, optional): Maximum context window size in tokens. Auto-inferred from `model_identifier` for known models; recommended when `model_identifier` is not in the registry.
    monitoring_endpoint (str, optional): Monitoring endpoint URL
    owner_id (str, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_LLM is evaluated against the proposed LLM and owner.
    provider_type (LLMProviderType, optional): Provider backend — one of `"OPENAI"`, `"LITELLM_PROXY"`, `"OPEN_ROUTER"`, `"VLLM"`, `"OLLAMA"`, `"LLAMA_CPP"`, `"CUSTOM_OPENAI_COMPATIBLE"`. Use `"CUSTOM_OPENAI_COMPATIBLE"` for third-party OpenAI-compatible endpoints such as Anthropic, Google Gemini, or Mistral. Auto-inferred from `model_identifier` for known models; required when `model_identifier` is not in the registry.
    supported_modalities (list[Modality], optional, server default="['TEXT']"): Modalities supported by this LLM (e.g. `["TEXT"]`). Auto-inferred from `model_identifier` for known models; defaults to `["TEXT"]` on the server if omitted.
    version (str, optional): Version information

Returns:
    CreateLLMResponse

```python
llms.create(*, display_name: 'str', model_identifier: 'str', api_key: 'str | None' = None, api_path: 'str | None' = None, capabilities: 'LLMCapabilities | None' = None, client_config: 'dict[str, Any] | None' = None, credentials: 'EndpointAuthentication | None' = None, dashscope_api_dialect: 'DashScopeApiDialect | None' = None, default_sampling_params: 'LLMSamplingParams | None' = None, description: 'str | None' = None, endpoint_url: 'str | None' = None, labels: 'dict[str, str] | None' = None, llm_id: 'str | None' = None, max_context_length: 'int | None' = None, monitoring_endpoint: 'str | None' = None, owner_id: 'str | None' = None, provider_type: 'LLMProviderType | None' = None, supported_modalities: 'list[Modality] | None' = None, version: 'str | None' = None) -> 'CreateLLMResponse'
```

[llms](../llms.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](../models/DashScopeApiDialect.md)
- [EndpointAuthentication](../models/EndpointAuthentication.md)
- [LLMCapabilities](../models/LLMCapabilities.md)
- [LLMProviderType](../models/LLMProviderType.md)
- [LLMSamplingParams](../models/LLMSamplingParams.md)
- [Modality](../models/Modality.md)
