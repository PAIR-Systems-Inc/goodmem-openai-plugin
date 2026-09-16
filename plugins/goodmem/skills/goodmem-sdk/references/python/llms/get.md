<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# llms.get

Get an LLM by ID

Retrieves the details of a specific LLM configuration by its unique identifier. Requires READ_LLM on the requested LLM. The service distinguishes a missing LLM from an existing LLM the caller cannot read. This is a read-only operation with no side effects.

Args:
    id (str): The unique identifier of the LLM to retrieve
    include_credentials (bool, optional, default=False): Whether to return stored credentials. Also accepts include_credentials. Requires READ_LLM_CREDENTIALS in addition to READ_LLM.

Returns:
    LLMResponse

```python
llms.get(*, id: 'str', include_credentials: 'bool | None' = None) -> 'LLMResponse'
```

[llms](../llms.md) · [Python](../../python.md)
