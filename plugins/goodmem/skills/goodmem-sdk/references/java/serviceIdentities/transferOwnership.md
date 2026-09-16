<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# serviceIdentities.transferOwnership

Transfer service-identity ownership

Transfers administrative ownership to another active principal. A service identity cannot own itself. The service identity's subject, immutable creator, credentials, grants, and roles are unchanged.

```java
TransferServiceIdentityOwnershipResponse transferOwnership(String id, TransferOwnershipRequest request)
```

```java
TransferServiceIdentityOwnershipResponse transferOwnership(java.util.UUID id, TransferOwnershipRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[serviceIdentities](../serviceIdentities.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
