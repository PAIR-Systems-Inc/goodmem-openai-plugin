<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# SpaceListOptions

Typed query options for `client.spaces.list`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 SpaceListOptions opts = SpaceListOptions.builder()
     .ownerId(UserId.from("value"))
     .build();

```

- `ownerId` (`UserId`): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-space READ_SPACE filtering.
- `nameFilter` (`String`): Filter spaces by name using glob pattern matching
- `maxResults` (`Integer`): Maximum number of results to return in a single page (defaults to 50, clamped to [1, 1000])
- `nextToken` (`String`): Pagination token for retrieving the next set of results
- `sortBy` (`SpacesListSortBy`): Field to sort by: 'created_time', 'updated_time', or 'name' (default: 'created_time'). Unsupported values return INVALID_ARGUMENT.
- `sortOrder` (`SortOrder`): Sort order (ASCENDING or DESCENDING, default: DESCENDING)
- `label` (`java.util.Map<String, String>`): Filter by label key-value pairs. Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

[Java](../../java.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
- [SpacesListSortBy](SpacesListSortBy.md)
- [UserId](UserId.md)
