<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.retrieve_memory_log_policies.get

Get a RetrieveMemory log policy

Retrieves a live RetrieveMemory log policy by UUID, or a tombstoned policy when include_deleted is true.

Args:
    id (str): The UUID of the policy to retrieve
    include_deleted (bool, optional, default=False): Whether to include tombstoned policies. Also accepts include_deleted.

Returns:
    RetrieveMemoryLogPolicy

```python
admin.retrieve_memory_log_policies.get(*, id: 'str', include_deleted: 'bool | None' = None) -> 'RetrieveMemoryLogPolicy'
```

[admin.retrieve_memory_log_policies](../admin.retrieve_memory_log_policies.md) · [Python](../../python.md)
