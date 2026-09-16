<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.list

List LLMs

Retrieves a list of LLM configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_LLM on the GoodMem instance. Each returned LLM must also be visible through READ_LLM; unauthorized LLMs are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

```java
java.util.List<LLMResponse> list()
```

No-filter convenience. Equivalent to passing `null` or a default LLMListOptions.

```java
java.util.List<LLMResponse> list(LLMListOptions options)
```

Typed-options overload. See `LLMListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[llms](../llms.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [LLMListOptions](../models/LLMListOptions.md)
