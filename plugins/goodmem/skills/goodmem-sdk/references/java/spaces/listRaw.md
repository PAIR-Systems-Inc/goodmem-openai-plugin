<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.listRaw

List spaces

Retrieves a list of spaces accessible to the caller, with optional filtering by owner, labels, and name. Results are paginated with a maximum number of spaces per response.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_SPACE on the GoodMem instance. Each returned space must also be visible through READ_SPACE; unauthorized spaces are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

DEFAULT SORT: Results ordered by created_at DESCENDING unless specified otherwise.

MAX_RESULTS CLAMPING: maxResults defaults to 50 and is clamped to [1, 1000] range.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
ai.pairsys.goodmem.client.Page<Space> listRaw(java.util.Map<String, Object> query)
```

[spaces](../spaces.md) · [Java](../../java.md)
