<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# apikeys.create

Issues a new API key and returns its raw value exactly once. Omitted subject and authorityMode create a self-issued human key that inherits the subject's live authority. A SCOPED key requires a nonempty immutable ceiling, and every ceiling rule must be conservatively covered by both the subject's live authority and the issuing credential's effective authority. A scoped issuer can create only scoped children. SERVICE subjects require SCOPED mode and MANAGE_ACCESS on the service identity.

AUTHORIZATION: Requires CREATE_API_KEY on the proposed credential; subject and ceiling checks are repeated by the final insertion statement.

```ts
create(request: CreateApiKeyRequest, requestOptions?: RequestOptions): Promise<CreateApiKeyResponseShape>
```

[apikeys](../apikeys.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [CreateApiKeyRequest](../models/CreateApiKeyRequest.md)
- [RequestOptions](../models/RequestOptions.md)
