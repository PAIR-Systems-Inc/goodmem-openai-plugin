<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.list

List human users

Requires LIST_USER on the GoodMem instance and READ_USER on each returned row. Authorization, label filtering, lifecycle filtering, and keyset pagination run in PostgreSQL. includeDeleted expands the lifecycle view but grants no access. includeEnrollmentSummary requests non-secret bootstrap posture only on active rows where MANAGE_USER_ENROLLMENT is independently authorized.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

```java
ai.pairsys.goodmem.client.Page<UserResponse> list(java.util.Map<String, Object> query)
```

[users](../users.md) · [Java](../../java.md)
