<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# admin.retrieveMemoryLogPoliciesList

Lists RetrieveMemory log policies with optional tombstone, active-time, name, label, sort, and pagination filters.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

```ts
retrieveMemoryLogPoliciesList(options?: AdminRetrieveMemoryLogPoliciesListOptions, requestOptions?: RequestOptions): Promise<Page<RetrieveMemoryLogPolicyResponseShape>>
```

[admin](../admin.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AdminRetrieveMemoryLogPoliciesListOptions](../models/AdminRetrieveMemoryLogPoliciesListOptions.md)
- [RequestOptions](../models/RequestOptions.md)
