<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# embedders.create

Create a new embedder

Creates an embedder configuration for use with memory spaces. If owner_id is omitted, the authenticated principal becomes the owner; CREATE_EMBEDDER is evaluated against that proposed embedder and owner. Returns 409 when an equivalent embedder configuration already exists for the owner. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

Args:
    display_name (str): User-facing name of the embedder
    model_identifier (str): The string that identifies the embedder. Usually the model identifier assigned by HuggingFace or the LLM provider, e.g., `"text-embedding-3-small"` by OpenAI. When a known model, auto-fills `provider_type`, `endpoint_url`, `dimensionality`, `max_sequence_length`, and `supported_modalities`.
    api_key (str, optional): Converts a plain API key string to the full `EndpointAuthentication` structure (i.e. `{"kind": "CREDENTIAL_KIND_API_KEY", "api_key": {"inline_secret": "sk-..."}}`). Use this for providers configured with API-key authentication. Gemini also supports ADC, which must be supplied through `credentials` instead.
    api_path (str, optional): Provider-relative request path. Omit or send blank to use the provider default. For Gemini, this is an API version: /v1beta for Developer and /v1 for Google Cloud.
    credentials (EndpointAuthentication, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
    dashscope_api_dialect (DashScopeApiDialect, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from api_path, the model catalog, or the native text default.
    description (str, optional): Description of the embedder
    dimensionality (int, optional): Output vector dimensions. Auto-inferred from `model_identifier` for known models (using `dimensions.default` from the model registry); required when `model_identifier` is not in the model registry.
    distribution_type (DistributionType, optional, SDK default='"DENSE"'): The distribution type of the embedder's vector output. Defaults to `"DENSE"` when not specified.
    embedder_id (str, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
    endpoint_url (str, optional): Base URL for the embedding endpoint. Auto-inferred from `provider_type` for providers with one canonical base URL. Gemini has distinct Developer and Google Cloud endpoints, so supply the URL that matches `gemini_endpoint_config`.
    gemini_endpoint_config (GeminiEndpointConfig, optional): Gemini backend routing. Valid only for the GEMINI provider. Omit to use the Developer API; when present, backend is required and the gRPC service validates the backend-specific project_id and location contract.
    labels (dict[str, str], optional): User-defined labels for categorization
    max_sequence_length (int, optional): Maximum token length accepted by the model. Auto-inferred from `model_identifier` for known models; required when `model_identifier` is not in the registry.
    monitoring_endpoint (str, optional): Monitoring endpoint URL
    owner_id (str, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_EMBEDDER is evaluated against the proposed embedder and owner.
    provider_type (ProviderType, optional): Provider backend — one of `"OPENAI"`, `"VLLM"`, `"TEI"`, `"LLAMA_CPP"`, `"VOYAGE"`, `"COHERE"`, `"JINA"`, `"DASHSCOPE"`, or `"GEMINI"`. Use `"GEMINI"` for the native Gemini embedding provider and select its API surface with `gemini_endpoint_config`. Auto-inferred from `model_identifier` for known catalog models.
    supported_modalities (list[Modality], optional, server default="['TEXT']"): Modalities supported by this embedder (e.g. `["TEXT"]`). Auto-inferred from `model_identifier` for known models; required when `model_identifier` is not in the registry.
    version (str, optional): Version information

Returns:
    EmbedderResponse

```python
embedders.create(*, display_name: 'str', model_identifier: 'str', api_key: 'str | None' = None, api_path: 'str | None' = None, credentials: 'EndpointAuthentication | None' = None, dashscope_api_dialect: 'DashScopeApiDialect | None' = None, description: 'str | None' = None, dimensionality: 'int | None' = None, distribution_type: 'DistributionType' = 'DENSE', embedder_id: 'str | None' = None, endpoint_url: 'str | None' = None, gemini_endpoint_config: 'GeminiEndpointConfig | None' = None, labels: 'dict[str, str] | None' = None, max_sequence_length: 'int | None' = None, monitoring_endpoint: 'str | None' = None, owner_id: 'str | None' = None, provider_type: 'ProviderType | None' = None, supported_modalities: 'list[Modality] | None' = None, version: 'str | None' = None) -> 'EmbedderResponse'
```

[embedders](../embedders.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](../models/DashScopeApiDialect.md)
- [DistributionType](../models/DistributionType.md)
- [EndpointAuthentication](../models/EndpointAuthentication.md)
- [GeminiEndpointConfig](../models/GeminiEndpointConfig.md)
- [Modality](../models/Modality.md)
- [ProviderType](../models/ProviderType.md)
