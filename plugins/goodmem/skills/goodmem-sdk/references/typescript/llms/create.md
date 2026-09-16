<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# llms.create

Creates a new LLM configuration for text generation services. LLMs represent connections to different language model API services (like OpenAI, vLLM, etc.) and include all the necessary configuration to use them for text generation.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another LLM exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison. The apiPath field defaults to '/chat/completions' if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_LLM is evaluated against the proposed LLM and owner.

```ts
create(request: LlmsCreateKnownWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<CreateLLMResponseShape>
create(request: LlmsCreateKnownWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<CreateLLMResponseShape>
create(request: LlmsCreateCustomWithCredentialsRequest, requestOptions?: ProviderNoApiKeyOptions): Promise<CreateLLMResponseShape>
create(request: LlmsCreateCustomWithoutCredentialsRequest, requestOptions?: ProviderApiKeyOptions): Promise<CreateLLMResponseShape>
```

[llms](../llms.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LlmsCreateCustomWithCredentialsRequest](../models/LlmsCreateCustomWithCredentialsRequest.md)
- [LlmsCreateCustomWithoutCredentialsRequest](../models/LlmsCreateCustomWithoutCredentialsRequest.md)
- [LlmsCreateKnownWithCredentialsRequest](../models/LlmsCreateKnownWithCredentialsRequest.md)
- [LlmsCreateKnownWithoutCredentialsRequest](../models/LlmsCreateKnownWithoutCredentialsRequest.md)
- [ProviderApiKeyOptions](../models/ProviderApiKeyOptions.md)
- [ProviderNoApiKeyOptions](../models/ProviderNoApiKeyOptions.md)
