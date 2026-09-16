<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.drain

Request the server to enter drain mode

Initiates drain mode and optionally waits for the server to quiesce.

Args:
    reason (str, optional): Human-readable reason for initiating drain mode.
    timeout_sec (int, optional, server default=900): Maximum seconds to wait for the server to quiesce before returning.
    wait_for_quiesce (bool, optional): If true, wait for in-flight requests to complete and the server to reach QUIESCED before responding.

Returns:
    AdminDrainResponse

```python
admin.drain(*, reason: 'str | None' = None, timeout_sec: 'int | None' = None, wait_for_quiesce: 'bool | None' = None) -> 'AdminDrainResponse'
```

[admin](../admin.md) · [Python](../../python.md)
