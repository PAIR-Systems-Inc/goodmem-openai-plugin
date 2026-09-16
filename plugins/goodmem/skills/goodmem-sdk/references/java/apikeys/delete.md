<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# apikeys.delete

Delete an API key

Permanently revokes an API key and immediately rejects it for future authentication. The durable credential and audit history remain stored. This operation requires DELETE_API_KEY and records the revocation time and actor; it cannot be undone. PUT /v1/apikeys/{id} with status=INACTIVE performs the same protected lifecycle transition.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.ApiKeyId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[apikeys](../apikeys.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyId](../models/ApiKeyId.md)
