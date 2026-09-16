<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# spaces.list

List spaces

Retrieves a list of spaces accessible to the caller, with optional filtering by owner, labels, and name. Results are paginated with a maximum number of spaces per response.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_SPACE on the GoodMem instance. Each returned space must also be visible through READ_SPACE; unauthorized spaces are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

DEFAULT SORT: Results ordered by created_at DESCENDING unless specified otherwise.

MAX_RESULTS CLAMPING: maxResults defaults to 50 and is clamped to [1, 1000] range.

```java
ai.pairsys.goodmem.client.Page<Space> list()
```

No-filter convenience. Equivalent to passing `null` or a default SpaceListOptions.

```java
ai.pairsys.goodmem.client.Page<Space> list(SpaceListOptions options)
```

Typed-options overload. See `SpaceListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[spaces](../spaces.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [SpaceListOptions](../models/SpaceListOptions.md)
