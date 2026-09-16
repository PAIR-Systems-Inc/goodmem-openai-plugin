<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.create

Creates one dormant human user after requiring instance-wide CREATE_USER authority. Creation does not issue a credential or create a role, grant, or authentication mapping.

```ts
create(request: CreateUserRequest, requestOptions?: RequestOptions): Promise<UserResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [CreateUserRequest](../models/CreateUserRequest.md)
- [RequestOptions](../models/RequestOptions.md)
