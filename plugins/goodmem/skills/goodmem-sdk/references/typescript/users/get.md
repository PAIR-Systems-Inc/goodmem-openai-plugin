<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.get

Returns a user selected by UUID after applying READ_USER authority. includeDeleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority.

```ts
get(options: UsersGetOptions, requestOptions?: RequestOptions): Promise<UserResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UsersGetOptions](../models/UsersGetOptions.md)
