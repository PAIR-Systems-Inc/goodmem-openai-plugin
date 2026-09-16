<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# serviceIdentities.list

Requires LIST_SERVICE_IDENTITY on the GoodMem instance and READ_SERVICE_IDENTITY on each returned row. Owner and label filters, lifecycle filtering, authorization, and keyset pagination execute in PostgreSQL.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

```ts
list(options?: ServiceIdentitiesListOptions, requestOptions?: RequestOptions): Promise<Page<ServiceIdentityResponseShape>>
```

[serviceIdentities](../serviceIdentities.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [ServiceIdentitiesListOptions](../models/ServiceIdentitiesListOptions.md)
