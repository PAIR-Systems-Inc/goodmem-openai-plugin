<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# users.getByUsername

Returns a user selected by exact username after applying READ_USER authority. includeDeleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority. Missing and unauthorized matches both return 404 so this guessable identifier cannot reveal whether a user exists.

```ts
getByUsername(username: string, options?: UsersGetByUsernameOptions, requestOptions?: RequestOptions): Promise<UserResponseShape>
```

[users](../users.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
- [UsersGetByUsernameOptions](../models/UsersGetByUsernameOptions.md)
