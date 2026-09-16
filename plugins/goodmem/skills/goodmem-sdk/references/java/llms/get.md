<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.get

Get an LLM by ID

Retrieves the details of a specific LLM configuration by its unique identifier. Requires READ_LLM on the requested LLM. The service distinguishes a missing LLM from an existing LLM the caller cannot read. This is a read-only operation with no side effects.

```java
LLMResponse get(String id)
```

No-filter convenience. Equivalent to passing `null` or a default LLMGetOptions.

```java
LLMResponse get(String id, LLMGetOptions options)
```

Typed-options overload. See `LLMGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
LLMResponse get(ai.pairsys.goodmem.client.models.LlmId id)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
LLMResponse get(ai.pairsys.goodmem.client.models.LlmId id, LLMGetOptions options)
```

Domain-ID typed overload. See `LLMGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
LLMResponse get(java.util.UUID id)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
LLMResponse get(java.util.UUID id, LLMGetOptions options)
```

UUID-typed overload. See `LLMGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[llms](../llms.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [LLMGetOptions](../models/LLMGetOptions.md)
- [LlmId](../models/LlmId.md)
