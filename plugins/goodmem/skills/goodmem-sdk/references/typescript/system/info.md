<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# system.info

Returns the server's advertised semantic version, git metadata, build timestamp, and optional capability flags. The endpoint is intentionally unauthenticated so bootstrap tooling can call it before API keys exist.

```ts
info(requestOptions?: RequestOptions): Promise<SystemInfoResponseShape>
```

[system](../system.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RequestOptions](../models/RequestOptions.md)
