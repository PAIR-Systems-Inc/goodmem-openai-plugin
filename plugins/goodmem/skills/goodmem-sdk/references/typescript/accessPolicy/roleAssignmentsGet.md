<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.roleAssignmentsGet

Reads one live assignment, or one revoked historical assignment when includeRevoked is true, after requiring MANAGE_ACCESS on its policy target.

```ts
roleAssignmentsGet(id: string, options?: AccessPolicyRoleAssignmentsGetOptions, requestOptions?: RequestOptions): Promise<RoleAssignmentResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AccessPolicyRoleAssignmentsGetOptions](../models/AccessPolicyRoleAssignmentsGetOptions.md)
- [RequestOptions](../models/RequestOptions.md)
