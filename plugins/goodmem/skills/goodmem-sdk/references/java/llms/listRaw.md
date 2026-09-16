<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.listRaw

List LLMs

Retrieves a list of LLM configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_LLM on the GoodMem instance. Each returned LLM must also be visible through READ_LLM; unauthorized LLMs are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
java.util.List<LLMResponse> listRaw(java.util.Map<String, Object> query)
```

[llms](../llms.md) · [Java](../../java.md)
