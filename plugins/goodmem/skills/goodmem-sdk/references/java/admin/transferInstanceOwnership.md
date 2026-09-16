<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# admin.transferInstanceOwnership

Transfer GoodMem instance ownership

Transfers the singleton GoodMem instance to another active human principal. Only the current instance owner may invoke this operation; ADMIN, MANAGE_ACCESS, and ordinary grants are insufficient. Ownership and the synthetic ROOT assignment move atomically. All ordinary roles, including ADMIN, remain unchanged. No credential is created or returned. After an unknown outcome, read the current owner before retrying.

```java
TransferInstanceOwnershipResponse transferInstanceOwnership(TransferOwnershipRequest request)
```

[admin](../admin.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
