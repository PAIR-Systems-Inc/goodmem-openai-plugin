<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.listRaw

List memories in a space

Lists all memories within a given space. Pagination is supported via maxResults and nextToken (opaque). nextToken is a URL-safe Base64 string without padding; do not parse or construct it. This is a read-only operation with no side effects and is safe to retry.

AUTHORIZATION: Requires LIST_MEMORY on the exact containing space. Each returned memory must also satisfy READ_MEMORY, either directly or through DIRECT_MEMBERS_OF that space. Both predicates are evaluated in PostgreSQL. Returns NOT_FOUND if the specified space does not exist.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
ai.pairsys.goodmem.client.Page<Memory> listRaw(String spaceId, java.util.Map<String, Object> query)
```

[memories](../memories.md) · [Java](../../java.md)
