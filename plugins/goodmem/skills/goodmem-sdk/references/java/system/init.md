<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# system.init

Initialize the system

Initializes the system by creating a root user and API key. This endpoint should only be called once during first-time setup. If the system is already initialized, the endpoint will return a success response without creating new credentials.

```java
SystemInitResponse init()
```

[system](../system.md) · [Java](../../java.md)
