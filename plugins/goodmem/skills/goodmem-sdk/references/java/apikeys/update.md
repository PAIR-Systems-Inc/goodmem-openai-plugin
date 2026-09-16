<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# apikeys.update

Update an API key

Updates an existing API key's labels or lifecycle status. Key ID, subject, ownership, key material, validity window, and creation audit fields remain immutable. Label changes require UPDATE_API_KEY; setting status=INACTIVE permanently revokes the key and requires DELETE_API_KEY; a request doing both requires both operations. Revoked keys cannot be reactivated. Side effects include updating administrative audit fields and, for revocation, recording the revocation time and actor.

```java
ApiKeyResponse update(String id, UpdateApiKeyRequest request)
```

```java
ApiKeyResponse update(ai.pairsys.goodmem.client.models.ApiKeyId id, UpdateApiKeyRequest request)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

```java
ApiKeyResponse update(java.util.UUID id, UpdateApiKeyRequest request)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on each promoted argument.

[apikeys](../apikeys.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyId](../models/ApiKeyId.md)
- [UpdateApiKeyRequest](../models/UpdateApiKeyRequest.md)
