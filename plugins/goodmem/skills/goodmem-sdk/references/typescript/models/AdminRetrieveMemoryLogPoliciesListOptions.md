<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AdminRetrieveMemoryLogPoliciesListOptions

- `includeDeleted` (`boolean`, optional): Whether to include tombstoned policies. Also accepts include_deleted.
- `nameFilter` (`string`, optional): Case-insensitive substring filter on policy display names. Also accepts name_filter.
- `activeAt` (`number`, optional): Only return policies active at this millisecond epoch timestamp. Also accepts active_at.
- `maxResults` (`number`, optional): Maximum number of policies to return. Also accepts max_results.
- `nextToken` (`string`, optional): Opaque pagination token returned by the previous list response. Also accepts next_token.
- `sortBy` (`"created_at" | "updated_at" | "display_name"`, optional): Sort field: created_at, updated_at, or display_name. Also accepts sort_by.
- `sortOrder` (`SortOrder`, optional): Sort order. Also accepts sort_order.
- `label` (`Record<string, string>`, optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
