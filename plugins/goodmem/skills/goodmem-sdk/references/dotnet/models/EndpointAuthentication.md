<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# EndpointAuthentication

Structured credential payload describing how GoodMem should authenticate with an upstream provider.

`Goodmem.Client.Models.EndpointAuthentication`

- `ApiKey` (`ApiKeyAuth?`): Configuration when kind is CREDENTIAL_KIND_API_KEY JSON: `apiKey`.
- `GcpAdc` (`GcpAdcAuth?`): Configuration when kind is CREDENTIAL_KIND_GCP_ADC JSON: `gcpAdc`.
- `Kind` (`CredentialKind`, required): Selected credential strategy JSON: `kind`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): Optional annotations to aid operators (e.g., "owner=vertex") JSON: `labels`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ApiKeyAuth](ApiKeyAuth.md)
- [CredentialKind](CredentialKind.md)
- [GcpAdcAuth](GcpAdcAuth.md)
