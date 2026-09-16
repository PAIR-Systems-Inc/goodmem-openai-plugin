<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# system.init

Initialize the system

Initializes the system by creating a root user and API key. This endpoint should only be called once during first-time setup. If the system is already initialized, the endpoint will return a success response without creating new credentials.

Returns:
    SystemInitResponse

```python
system.init() -> 'SystemInitResponse'
```

[system](../system.md) · [Python](../../python.md)
