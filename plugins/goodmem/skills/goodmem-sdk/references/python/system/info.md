<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# system.info

Retrieve server build metadata

Returns the server's advertised semantic version, git metadata, build timestamp, and optional capability flags. The endpoint is intentionally unauthenticated so bootstrap tooling can call it before API keys exist.

Returns:
    SystemInfoResponse

```python
system.info() -> 'SystemInfoResponse'
```

[system](../system.md) · [Python](../../python.md)
