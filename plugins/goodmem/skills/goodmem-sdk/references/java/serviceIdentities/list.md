<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# serviceIdentities.list

List service identities

Requires LIST_SERVICE_IDENTITY on the GoodMem instance and READ_SERVICE_IDENTITY on each returned row. Owner and label filters, lifecycle filtering, authorization, and keyset pagination execute in PostgreSQL.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

```java
ai.pairsys.goodmem.client.Page<ServiceIdentityResponse> list(java.util.Map<String, Object> query)
```

[serviceIdentities](../serviceIdentities.md) · [Java](../../java.md)
