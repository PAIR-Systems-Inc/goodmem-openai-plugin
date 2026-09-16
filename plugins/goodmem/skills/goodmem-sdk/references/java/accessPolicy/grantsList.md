<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# accessPolicy.grantsList

List authorization grants

Lists grants attached to one resource. MANAGE_ACCESS is required on that resource; continuation tokens are bound to the caller and filters.

```java
ai.pairsys.goodmem.client.Page<AuthorizationGrant> grantsList(java.util.Map<String, Object> query)
```

[accessPolicy](../accessPolicy.md) · [Java](../../java.md)
