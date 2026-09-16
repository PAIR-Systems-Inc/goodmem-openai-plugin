<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ServiceIdentitiesListOptions

- `ownerPrincipalId` (`string`, optional): Exact current administrative-owner principal UUID
- `includeDeleted` (`boolean`, optional): Include readable permanent tombstones
- `maxResults` (`number`, optional): Page size; defaults to 50 and must be between 1 and 1000
- `nextToken` (`string`, optional): Opaque continuation token
- `label` (`Record<string, string>`, optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

[TypeScript](../../typescript.md)
