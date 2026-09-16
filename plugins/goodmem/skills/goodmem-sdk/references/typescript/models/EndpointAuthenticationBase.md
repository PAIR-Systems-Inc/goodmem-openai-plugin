<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EndpointAuthenticationBase

- `kind` (`CredentialKind`, required): Selected credential strategy
- `apiKey` (`ApiKeyAuth | null`, optional): Configuration when kind is CREDENTIAL_KIND_API_KEY
- `gcpAdc` (`GcpAdcAuth | null`, optional): Configuration when kind is CREDENTIAL_KIND_GCP_ADC
- `labels` (`Record<string, string> | null`, optional): Optional annotations to aid operators (e.g., "owner=vertex")

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ApiKeyAuth](ApiKeyAuth.md)
- [CredentialKind](CredentialKind.md)
- [GcpAdcAuth](GcpAdcAuth.md)
