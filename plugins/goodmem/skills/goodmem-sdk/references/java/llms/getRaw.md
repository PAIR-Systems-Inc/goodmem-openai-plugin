<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.getRaw

Get an LLM by ID

Retrieves the details of a specific LLM configuration by its unique identifier. Requires READ_LLM on the requested LLM. The service distinguishes a missing LLM from an existing LLM the caller cannot read. This is a read-only operation with no side effects.

Escape hatch. Prefer the typed sibling `get(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
LLMResponse getRaw(String id, java.util.Map<String, Object> query)
```

[llms](../llms.md) · [Java](../../java.md)
