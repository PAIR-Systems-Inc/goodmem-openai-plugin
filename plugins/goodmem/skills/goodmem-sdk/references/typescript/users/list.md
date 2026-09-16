<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.list

Requires LIST_USER on the GoodMem instance and READ_USER on each returned row. Authorization, label filtering, lifecycle filtering, and keyset pagination run in PostgreSQL. includeDeleted expands the lifecycle view but grants no access. includeEnrollmentSummary requests non-secret bootstrap posture only on active rows where MANAGE_USER_ENROLLMENT is independently authorized.

LABEL FILTERS: Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

```ts
list(options?: UsersListOptions, requestOptions?: RequestOptions): Promise<Page<UserResponseShape>>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UsersListOptions](../models/UsersListOptions.md)
