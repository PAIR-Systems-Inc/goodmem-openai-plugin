<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# system.info

Retrieve server build metadata

Returns the server's advertised semantic version, git metadata, build timestamp, and optional capability flags. The endpoint is intentionally unauthenticated so bootstrap tooling can call it before API keys exist.

```java
SystemInfoResponse info()
```

[system](../system.md) · [Java](../../java.md)
