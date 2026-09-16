<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# apikeys.get

Get an API key

Returns complete non-secret metadata for one existing credential after requiring effective READ_API_KEY authority. The immutable ceiling is always complete and ceilingOmitted is false. Raw key material and hashes are never returned.

```java
ApiKeyResponse get(String id)
```

```java
ApiKeyResponse get(ai.pairsys.goodmem.client.models.ApiKeyId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
ApiKeyResponse get(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[apikeys](../apikeys.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyId](../models/ApiKeyId.md)
