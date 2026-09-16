<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.getEnrollment

Returns non-secret metadata for one current or historical enrollment. The target user is resolved before the enrollment, and MANAGE_USER_ENROLLMENT with ANY or EXACT authority on that user is required. Raw enrollment tokens are never returned.

```ts
getEnrollment(userId: string, enrollmentId: string, requestOptions?: RequestOptions): Promise<UserEnrollmentResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
