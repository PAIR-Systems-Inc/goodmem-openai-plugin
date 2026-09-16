<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.listEnrollments

Returns one newest-first page containing pending, expired, consumed, and revoked enrollment metadata. MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user is required. The page never contains raw credentials.

```ts
listEnrollments(userId: string, options?: UsersListEnrollmentsOptions, requestOptions?: RequestOptions): Promise<Page<UserEnrollmentResponseShape>>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UsersListEnrollmentsOptions](../models/UsersListEnrollmentsOptions.md)
