<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# admin.retrieveMemoryLogPoliciesList

List RetrieveMemory log policies

Lists RetrieveMemory log policies with optional tombstone, active-time, name, label, sort, and pagination filters.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

```java
ai.pairsys.goodmem.client.Page<RetrieveMemoryLogPolicy> retrieveMemoryLogPoliciesList(java.util.Map<String, Object> query)
```

[admin](../admin.md) · [Java](../../java.md)
