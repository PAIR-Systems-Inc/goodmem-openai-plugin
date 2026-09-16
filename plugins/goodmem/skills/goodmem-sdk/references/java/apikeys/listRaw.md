<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# apikeys.listRaw

List API keys

Requires LIST_API_KEY on the singleton instance, then retrieves one UUID-ordered page containing only credentials that independently pass READ_API_KEY. Both gates use the authenticated principal's live authority and any scoped-key ceiling. Subject, owner, and lifecycle filters are applied after authorization. FULL includes complete immutable ceilings; BASIC omits them, sets ceilingOmitted=true, and permits larger pages. Raw key values and key hashes are never returned.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
ai.pairsys.goodmem.client.Page<ApiKeyResponse> listRaw(java.util.Map<String, Object> query)
```

[apikeys](../apikeys.md) · [Java](../../java.md)
