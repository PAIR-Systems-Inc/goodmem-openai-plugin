<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.retrieve_memory_log_policies.delete

Delete a RetrieveMemory log policy

Idempotently tombstones an immutable RetrieveMemory log policy.

Args:
    id (str): The UUID of the policy to delete
    request (DeleteRetrieveMemoryLogPolicyRequest | dict | None, optional): Optional payload. Accepts a DeleteRetrieveMemoryLogPolicyRequest instance, a plain dict with the same fields, or ``None`` to send no body. Only specified fields are sent to the server.

Returns:
    RetrieveMemoryLogPolicy

```python
admin.retrieve_memory_log_policies.delete(*, id: 'str', request: 'DeleteRetrieveMemoryLogPolicyRequest | dict | None' = None) -> 'RetrieveMemoryLogPolicy'
```

[admin.retrieve_memory_log_policies](../admin.retrieve_memory_log_policies.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [DeleteRetrieveMemoryLogPolicyRequest](../models/DeleteRetrieveMemoryLogPolicyRequest.md)
