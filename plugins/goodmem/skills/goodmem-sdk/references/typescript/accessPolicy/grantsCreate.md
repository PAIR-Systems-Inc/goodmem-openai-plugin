<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.grantsCreate

Creates one direct grant after resolving its typed policy target and requiring MANAGE_ACCESS. Direct grants cannot confer credential-read or ownership-transfer authority. ALL_AUTHENTICATED grants require an assigned-resource selector. MANAGE_ACCESS and MANAGE_USER_ENROLLMENT require a concrete principal and ANY or EXACT; MANAGE_USER_ENROLLMENT with EXACT must target USER.

```ts
grantsCreate(request: CreateAuthorizationGrantRequest, requestOptions?: RequestOptions): Promise<AuthorizationGrantResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [CreateAuthorizationGrantRequest](../models/CreateAuthorizationGrantRequest.md)
- [RequestOptions](../models/RequestOptions.md)
