<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# serviceIdentities.update

Update a service identity

Updates only fields present in the request. Empty description clears that optional field. Ownership changes use the dedicated transfer endpoint.

```java
ServiceIdentityResponse update(String id, UpdateServiceIdentityRequest request)
```

```java
ServiceIdentityResponse update(java.util.UUID id, UpdateServiceIdentityRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[serviceIdentities](../serviceIdentities.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [UpdateServiceIdentityRequest](../models/UpdateServiceIdentityRequest.md)
