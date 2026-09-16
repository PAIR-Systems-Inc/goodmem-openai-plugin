<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# rerankers.create

Create a new reranker

Creates a new reranker configuration for ranking search results. Rerankers represent connections to different reranking API services (like TEI, OpenAI, etc.) and include all the necessary configuration to use them for result ranking.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another reranker exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison.

DEFAULTS: api_path defaults to '/v2/rerank' for Cohere and '/rerank' for other providers if omitted; supported_modalities defaults to [TEXT] if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless owner_id is provided; CREATE_RERANKER is evaluated against the proposed reranker and owner. This operation is NOT idempotent - each request creates a new reranker record.

Args:
    display_name (str): User-facing name of the reranker
    model_identifier (str): When a known model, auto-fills `provider_type`, `endpoint_url`, and `supported_modalities`.
    api_key (str, optional): Converts a plain API key string to the full `EndpointAuthentication` structure (i.e. `{"kind": "CREDENTIAL_KIND_API_KEY", "api_key": {"inline_secret": "sk-..."}}`).
    api_path (str, optional): API path for reranking request (defaults: Cohere `/v2/rerank`, Jina `/v1/rerank`, others `/rerank`).
    credentials (EndpointAuthentication, optional): Structured credential payload describing how to authenticate with the provider. Required for SaaS providers; optional for local or proxy providers.
    dashscope_api_dialect (DashScopeApiDialect, optional): DashScope request and response API dialect. Valid only for the DASHSCOPE provider. Omit to infer the dialect from api_path, the model catalog, or the native reranking default.
    description (str, optional): Description of the reranker
    endpoint_url (str, optional): Base URL for the reranking endpoint. Auto-inferred from `provider_type` for known providers; required when `model_identifier` is not in the registry.
    labels (dict[str, str], optional): User-defined labels for categorization
    monitoring_endpoint (str, optional): Monitoring endpoint URL
    owner_id (str, optional): Optional owner principal UUID. If omitted, defaults to the authenticated principal. CREATE_RERANKER is evaluated against the proposed reranker and owner.
    provider_type (ProviderType, optional): Provider backend (e.g. `"COHERE"`, `"JINA"`). Auto-inferred from `model_identifier` for known models; required when `model_identifier` is not in the registry.
    reranker_id (str, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
    supported_modalities (list[Modality], optional, server default="['TEXT']"): Modalities supported by this reranker (e.g. `["TEXT"]`). Auto-inferred from `model_identifier` for known models; defaults to `["TEXT"]` on the server if omitted.
    version (str, optional): Version information

Returns:
    RerankerResponse

```python
rerankers.create(*, display_name: 'str', model_identifier: 'str', api_key: 'str | None' = None, api_path: 'str | None' = None, credentials: 'EndpointAuthentication | None' = None, dashscope_api_dialect: 'DashScopeApiDialect | None' = None, description: 'str | None' = None, endpoint_url: 'str | None' = None, labels: 'dict[str, str] | None' = None, monitoring_endpoint: 'str | None' = None, owner_id: 'str | None' = None, provider_type: 'ProviderType | None' = None, reranker_id: 'str | None' = None, supported_modalities: 'list[Modality] | None' = None, version: 'str | None' = None) -> 'RerankerResponse'
```

[rerankers](../rerankers.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [DashScopeApiDialect](../models/DashScopeApiDialect.md)
- [EndpointAuthentication](../models/EndpointAuthentication.md)
- [Modality](../models/Modality.md)
- [ProviderType](../models/ProviderType.md)
