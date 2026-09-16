<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ApiKeyAuthBase

- `inlineSecret` (`string | null`, optional): Secret stored directly in GoodMem (mutually exclusive with secretRef)
- `secretRef` (`SecretReference | null`, optional): Reference to an external secret manager entry (mutually exclusive with inlineSecret)
- `headerName` (`string | null`, optional): Desired HTTP header to carry the credential (defaults to Authorization)
- `prefix` (`string | null`, optional): Optional prefix prepended to the secret (e.g., "Bearer ")

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [SecretReference](SecretReference.md)
