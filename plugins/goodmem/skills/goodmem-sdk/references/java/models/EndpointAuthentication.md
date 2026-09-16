<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# EndpointAuthentication

Structured credential payload describing how GoodMem should authenticate with an upstream provider.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `kind` (`CredentialKind`): Selected credential strategy
- `apiKey` (`ApiKeyAuth`): Configuration when kind is CREDENTIAL_KIND_API_KEY
- `gcpAdc` (`GcpAdcAuth`): Configuration when kind is CREDENTIAL_KIND_GCP_ADC
- `labels` (`java.util.Map<String, String>`): Optional annotations to aid operators (e.g., "owner=vertex")

[Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyAuth](ApiKeyAuth.md)
- [CredentialKind](CredentialKind.md)
- [GcpAdcAuth](GcpAdcAuth.md)
