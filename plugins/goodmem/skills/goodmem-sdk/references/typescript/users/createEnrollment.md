<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.createEnrollment

Creates a short-lived, one-time enrollment credential for an existing dormant human. Requires MANAGE_USER_ENROLLMENT with ANY or EXACT authority on the target user. The raw credential is returned only once. rotateExisting atomically revokes and replaces a live enrollment; an expired enrollment is replaced automatically.

```ts
createEnrollment(userId: string, requestOrRequestOptions?: CreateUserEnrollmentRequest | RequestOptions, requestOptions?: RequestOptions): Promise<CreateUserEnrollmentResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [CreateUserEnrollmentRequest](../models/CreateUserEnrollmentRequest.md)
- [RequestOptions](../models/RequestOptions.md)
