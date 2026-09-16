<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# apikeys.list

List API keys

Requires LIST_API_KEY on the singleton instance, then retrieves one UUID-ordered page containing only credentials that independently pass READ_API_KEY. Both gates use the authenticated principal's live authority and any scoped-key ceiling. Subject, owner, and lifecycle filters are applied after authorization. FULL includes complete immutable ceilings; BASIC omits them, sets ceilingOmitted=true, and permits larger pages. Raw key values and key hashes are never returned.

```java
ai.pairsys.goodmem.client.Page<ApiKeyResponse> list()
```

No-filter convenience. Equivalent to passing `null` or a default ApiKeyListOptions.

```java
ai.pairsys.goodmem.client.Page<ApiKeyResponse> list(ApiKeyListOptions options)
```

Typed-options overload. See `ApiKeyListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[apikeys](../apikeys.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyListOptions](../models/ApiKeyListOptions.md)
