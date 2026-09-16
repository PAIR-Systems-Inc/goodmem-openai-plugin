<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# instance.get

Get the GoodMem instance

Returns singleton instance identity, ownership, and audit metadata after requiring effective READ_INSTANCE authority. The built-in ADMIN role supplies this authority; instance ownership alone does not. A scoped API key must also retain READ_INSTANCE in its immutable ceiling. This operation does not expose credentials or mutate instance state.

```java
GoodMemInstance get()
```

[instance](../instance.md) · [Java](../../java.md)
