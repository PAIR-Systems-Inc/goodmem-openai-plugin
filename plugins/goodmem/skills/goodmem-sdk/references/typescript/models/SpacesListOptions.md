<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SpacesListOptions

- `ownerId` (`string`, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-space READ_SPACE filtering.
- `nameFilter` (`string`, optional): Filter spaces by name using glob pattern matching
- `maxResults` (`number`, optional): Maximum number of results to return in a single page (defaults to 50, clamped to [1, 1000])
- `nextToken` (`string`, optional): Pagination token for retrieving the next set of results
- `sortBy` (`"created_time" | "updated_time" | "name"`, optional): Field to sort by: 'created_time', 'updated_time', or 'name' (default: 'created_time'). Unsupported values return INVALID_ARGUMENT.
- `sortOrder` (`SortOrder`, optional): Sort order (ASCENDING or DESCENDING, default: DESCENDING)
- `label` (`Record<string, string>`, optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
