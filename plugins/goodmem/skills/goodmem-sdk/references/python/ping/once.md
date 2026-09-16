<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# ping.once

Run a single ping probe

Runs a single ping probe and returns the probe result. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

Args:
    target_id (str): Target resource ID (UUID)
    payload (str, optional): Explicit UTF-8 payload to send with the probe (mutually exclusive with payload_size_bytes)
    payload_size_bytes (int, optional): Synthetic payload size in bytes (mutually exclusive with payload)
    payload_type (PingPayloadType, optional): Desired payload type (defaults to provider-specific value)
    target_type_hint (PingTargetType, optional): Optional hint for the target resource type
    timeout_ms (int, optional, server default=5000): Per-probe timeout in milliseconds (0 uses server default)

Returns:
    PingResult

```python
ping.once(*, target_id: 'str', payload: 'str | None' = None, payload_size_bytes: 'int | None' = None, payload_type: 'PingPayloadType | None' = None, target_type_hint: 'PingTargetType | None' = None, timeout_ms: 'int | None' = None) -> 'PingResult'
```

[ping](../ping.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [PingPayloadType](../models/PingPayloadType.md)
- [PingTargetType](../models/PingTargetType.md)
