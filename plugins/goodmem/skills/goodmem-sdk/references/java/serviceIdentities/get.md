<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# serviceIdentities.get

Get a service identity

Returns a service identity after applying READ_SERVICE_IDENTITY authority. includeDeleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority.

```java
ServiceIdentityResponse get(String id, java.util.Map<String, Object> query)
```

```java
ServiceIdentityResponse get(java.util.UUID id, java.util.Map<String, Object> query)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[serviceIdentities](../serviceIdentities.md) · [Java](../../java.md)
