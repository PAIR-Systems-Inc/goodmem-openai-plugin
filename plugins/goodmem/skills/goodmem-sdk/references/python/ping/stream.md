<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# ping.stream

Stream ping probe results

Opens a streaming ping session and returns per-probe results plus a terminal summary. Requires both the target-specific PING operation and its corresponding EXECUTE operation: PING_EMBEDDER plus EXECUTE_EMBEDDER, PING_RERANKER plus EXECUTE_RERANKER, or PING_LLM plus EXECUTE_LLM.

Args:
    target_id (str): Target resource ID (UUID)
    count (int, optional, server default=4): Number of probes to run (0 uses server default)
    interval_ms (int, optional, server default=1000): Delay between probes in milliseconds (0 uses server default)
    jitter (bool, optional): Add jitter to probe scheduling
    labels (dict[str, str], optional): Optional labels to attach to the ping session
    max_in_flight (int, optional, server default=1): Maximum concurrent probes (defaults to 1)
    payload (str, optional): Explicit UTF-8 payload to send with each probe (mutually exclusive with payload_size_bytes)
    payload_size_bytes (int, optional): Synthetic payload size in bytes (mutually exclusive with payload)
    payload_type (PingPayloadType, optional): Desired payload type (defaults to provider-specific value)
    stream (bool, optional, SDK default=True): If `True` (default), returns a `PingStream` context manager that yields events as they arrive from the server. If `False`, collects all events and returns a plain `list[PingEvent]`.
    target_type_hint (PingTargetType, optional): Optional hint for the target resource type
    timeout_ms (int, optional, server default=5000): Per-probe timeout in milliseconds (0 uses server default)

Returns:
    PingStream | list[PingEvent]

```python
ping.stream(*, target_id: 'str', count: 'int | None' = None, interval_ms: 'int | None' = None, jitter: 'bool | None' = None, labels: 'dict[str, str] | None' = None, max_in_flight: 'int | None' = None, payload: 'str | None' = None, payload_size_bytes: 'int | None' = None, payload_type: 'PingPayloadType | None' = None, stream: 'bool' = True, target_type_hint: 'PingTargetType | None' = None, timeout_ms: 'int | None' = None) -> 'PingStream | list[PingEvent]'
```

[ping](../ping.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [PingPayloadType](../models/PingPayloadType.md)
- [PingTargetType](../models/PingTargetType.md)
