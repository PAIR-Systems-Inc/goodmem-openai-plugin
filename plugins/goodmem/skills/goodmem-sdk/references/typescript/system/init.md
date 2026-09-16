<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# system.init

Initializes the system by creating a root user and API key. This endpoint should only be called once during first-time setup. If the system is already initialized, the endpoint will return a success response without creating new credentials.

```ts
init(requestOptions?: RequestOptions): Promise<SystemInitResponseShape>
```

[system](../system.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
