<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# llms.list

List LLMs

Retrieves a list of LLM configurations accessible to the caller, with optional filtering.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_LLM on the GoodMem instance. Each returned LLM must also be visible through READ_LLM; unauthorized LLMs are filtered in PostgreSQL. The owner_id parameter filters that already-authorized result set and does not grant additional visibility. This is a read-only operation with no side effects.

Args:
    label (dict[str, str], optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).
    owner_id (str, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-LLM READ_LLM filtering.
    provider_type (LLMProviderType, optional): Filter LLMs by provider type. Allowed values match the LLMProviderType schema.

Returns:
    list[LLMResponse]

```python
llms.list(*, label: 'dict[str, str] | None' = None, owner_id: 'str | None' = None, provider_type: 'LLMProviderType | None' = None) -> 'list[LLMResponse]'
```

[llms](../llms.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [LLMProviderType](../models/LLMProviderType.md)
