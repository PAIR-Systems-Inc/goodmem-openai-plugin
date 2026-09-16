<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# ApiKeyAuth

Configuration for classic API-key authentication.

`Goodmem.Client.Models.ApiKeyAuth`

- `HeaderName` (`string?`): Desired HTTP header to carry the credential (defaults to Authorization) JSON: `headerName`.
- `InlineSecret` (`string?`): Secret stored directly in GoodMem (mutually exclusive with secretRef) JSON: `inlineSecret`.
- `Prefix` (`string?`): Optional prefix prepended to the secret (e.g., "Bearer ") JSON: `prefix`.
- `SecretRef` (`SecretReference?`): Reference to an external secret manager entry (mutually exclusive with inlineSecret) JSON: `secretRef`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [SecretReference](SecretReference.md)
