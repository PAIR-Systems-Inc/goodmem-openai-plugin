<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.update

Updates only fields present in the request. Empty username or displayName values clear those optional fields. Updating a deleted user fails with 412.

```ts
update(id: string, request: UpdateUserRequest, requestOptions?: RequestOptions): Promise<UserResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UpdateUserRequest](../models/UpdateUserRequest.md)
