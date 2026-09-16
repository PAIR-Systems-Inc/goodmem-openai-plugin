<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# llms.update

Update an LLM

Updates an existing LLM configuration including display information, endpoint configuration, model parameters, credentials, and labels. All fields are optional - only specified fields will be updated.

SUPPORTED_MODALITIES UPDATE: If the array contains >=1 elements, it replaces the stored set; if empty or omitted, no change occurs and it does not count as an update by itself.

IMPORTANT: provider_type is IMMUTABLE after creation and cannot be changed. Requires UPDATE_LLM on the requested LLM.

Args:
    id (str): The unique identifier of the LLM to update
    request (LLMUpdateRequest | dict): The request payload. Accepts a LLMUpdateRequest instance or a plain dict with the same fields.

Returns:
    LLMResponse

```python
llms.update(*, id: 'str', request: 'LLMUpdateRequest | dict') -> 'LLMResponse'
```

[llms](../llms.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [LLMUpdateRequest](../models/LLMUpdateRequest.md)
