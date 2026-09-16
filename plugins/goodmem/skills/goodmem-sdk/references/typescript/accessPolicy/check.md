<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# accessPolicy.check

Evaluates 1 to 50 concrete operation-and-target checks under the authenticated caller's live authority and any API-key ceiling. Results are positional and advisory: missing targets and denied operations both return allowed=false, and every later resource request performs fresh authorization. Top-level creates and LIST_API_KEY target INSTANCE; CREATE_MEMORY and LIST_MEMORY target their parent SPACE; reads, mutations, proxy operations, and access-policy administration target concrete resources. LIST_RETRIEVE_MEMORY_LOG_POLICY is rejected because its current candidate-based list rule has no instance-wide preflight.

```ts
check(request: CheckAuthorizationsRequest, requestOptions?: RequestOptions): Promise<CheckAuthorizationsResponseShape>
```

[accessPolicy](../accessPolicy.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [CheckAuthorizationsRequest](../models/CheckAuthorizationsRequest.md)
- [RequestOptions](../models/RequestOptions.md)
