<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.update

Update an LLM

Updates an existing LLM configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself.

IMPORTANT: providerType is IMMUTABLE after creation and cannot be changed. Requires UPDATE_LLM on the requested LLM.

```java
LLMResponse update(String id, LLMUpdateRequest request)
```

```java
LLMResponse update(ai.pairsys.goodmem.client.models.LlmId id, LLMUpdateRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
LLMResponse update(java.util.UUID id, LLMUpdateRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[llms](../llms.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [LLMUpdateRequest](../models/LLMUpdateRequest.md)
- [LlmId](../models/LlmId.md)
