<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EndpointAuthentication

Structured credential payload describing how GoodMem should authenticate with an upstream provider.

```ts

export type EndpointAuthentication = Prettify<Pick<EndpointAuthenticationBase, "labels"> & {
    kind: "CREDENTIAL_KIND_API_KEY";
    apiKey: ApiKeyAuth;
    gcpAdc?: null | undefined;
}> | Prettify<Pick<EndpointAuthenticationBase, "labels"> & {
    kind: "CREDENTIAL_KIND_GCP_ADC";
    apiKey?: null | undefined;
    gcpAdc: GcpAdcAuth;
}> | Prettify<Pick<EndpointAuthenticationBase, "labels"> & {
    kind: "CREDENTIAL_KIND_UNSPECIFIED";
    apiKey?: null | undefined;
    gcpAdc?: null | undefined;
}>;
```

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ApiKeyAuth](ApiKeyAuth.md)
- [EndpointAuthenticationBase](EndpointAuthenticationBase.md)
- [GcpAdcAuth](GcpAdcAuth.md)
