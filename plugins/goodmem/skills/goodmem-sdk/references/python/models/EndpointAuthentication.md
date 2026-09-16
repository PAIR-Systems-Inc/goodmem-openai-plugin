<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# EndpointAuthentication

Structured credential payload describing how GoodMem should authenticate with an upstream provider.

- `kind` (`CredentialKind | None`, required): Selected credential strategy
- `api_key` (`ApiKeyAuth | None`, optional): Configuration when kind is CREDENTIAL_KIND_API_KEY JSON: `apiKey`.
- `gcp_adc` (`GcpAdcAuth | None`, optional): Configuration when kind is CREDENTIAL_KIND_GCP_ADC JSON: `gcpAdc`.
- `labels` (`dict[str, str] | None`, optional): Optional annotations to aid operators (e.g., "owner=vertex")

[Python](../../python.md)

Related types — open only those used by your request:

- [ApiKeyAuth](ApiKeyAuth.md)
- [CredentialKind](CredentialKind.md)
- [GcpAdcAuth](GcpAdcAuth.md)
