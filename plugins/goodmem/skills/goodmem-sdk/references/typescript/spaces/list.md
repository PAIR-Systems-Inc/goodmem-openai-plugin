<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# spaces.list

Retrieves a list of spaces accessible to the caller, with optional filtering by owner, labels, and name. Results are paginated with a maximum number of spaces per response.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_SPACE on the GoodMem instance. Each returned space must also be visible through READ_SPACE; unauthorized spaces are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

DEFAULT SORT: Results ordered by created_at DESCENDING unless specified otherwise.

MAX_RESULTS CLAMPING: maxResults defaults to 50 and is clamped to [1, 1000] range.

```ts
list(options?: SpacesListOptions, requestOptions?: RequestOptions): Promise<Page<SpaceResponseShape>>
```

[spaces](../spaces.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [SpacesListOptions](../models/SpacesListOptions.md)
