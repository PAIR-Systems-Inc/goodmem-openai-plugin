<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.retrieve_memory_log_policies.create

Create a RetrieveMemory log policy

Creates an immutable administrative policy that can automatically enable durable RetrieveMemory request logging.

Args:
    policy_id (str, optional): Optional client-provided policy UUID.
    display_name (str): Human-readable policy name.
    description (str, optional): Optional operator description.
    condition (RetrieveMemoryLogPolicyCondition): Policy match condition.
    active_from (int, optional): Inclusive activation time in milliseconds since epoch.
    active_until (int, optional): Exclusive deactivation time in milliseconds since epoch.
    labels (dict[str, str], optional): Operator labels for listing and administration.

Returns:
    RetrieveMemoryLogPolicy

```python
admin.retrieve_memory_log_policies.create(*, display_name: 'str', condition: 'RetrieveMemoryLogPolicyCondition', policy_id: 'str | None' = None, description: 'str | None' = None, active_from: 'int | None' = None, active_until: 'int | None' = None, labels: 'dict[str, str] | None' = None) -> 'RetrieveMemoryLogPolicy'
```

[admin.retrieve_memory_log_policies](../admin.retrieve_memory_log_policies.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyCondition](../models/RetrieveMemoryLogPolicyCondition.md)
