<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.create

```java
CreateLLMResponse create(LLMCreationRequest request)
```

Create a new LLM

Creates a new LLM configuration for text generation services. LLMs represent connections to different language model API services (like OpenAI, vLLM, etc.) and include all the necessary configuration to use them for text generation.

DUPLICATE DETECTION: Returns HTTP 409 Conflict (ALREADY_EXISTS) if another LLM exists with the same effective provider connection and model configuration for this owner after endpoint canonicalization and provider-default resolution. Equivalent credentials participate in the comparison. The apiPath field defaults to '/chat/completions' if omitted.

OWNER DEFAULTS: Owner defaults to the authenticated principal unless ownerId is provided; CREATE_LLM is evaluated against the proposed LLM and owner.

```java
CreateLLMResponse create(LLMCreationRequest request, String apiKey)
```

Convenience overload: auto-fills provider / endpoint / dimensionality
 from the bundled model registry keyed by `modelIdentifier`,
 and converts a bare `apiKey` string to the structured
 `EndpointAuthentication`. Pass `null` for
 `apiKey` to preserve `request.credentials()`.
 Any field already set on `request` wins over registry values.

[llms](../llms.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [LLMCreationRequest](../models/LLMCreationRequest.md)
