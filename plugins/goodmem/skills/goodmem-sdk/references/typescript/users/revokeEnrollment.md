<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.revokeEnrollment

Permanently revokes one outstanding enrollment after requiring MANAGE_USER_ENROLLMENT on its target user. Repeating an authorized revocation succeeds without replacing its original audit provenance. Consumed enrollments cannot be revoked.

```ts
revokeEnrollment(userId: string, enrollmentId: string, requestOptions?: RequestOptions): Promise<void>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
