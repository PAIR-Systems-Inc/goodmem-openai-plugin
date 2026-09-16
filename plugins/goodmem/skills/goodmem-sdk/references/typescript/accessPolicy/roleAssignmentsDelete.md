<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.roleAssignmentsDelete

Soft-revokes one non-ROOT assignment and returns its durable historical row. Repeating the request is idempotent while the caller retains MANAGE_ACCESS.

```ts
roleAssignmentsDelete(id: string, requestOptions?: RequestOptions): Promise<RoleAssignmentResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
