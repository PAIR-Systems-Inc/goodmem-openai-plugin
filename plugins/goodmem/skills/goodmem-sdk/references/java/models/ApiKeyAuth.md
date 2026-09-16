<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ApiKeyAuth

Configuration for classic API-key authentication.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `inlineSecret` (`String`): Secret stored directly in GoodMem (mutually exclusive with secretRef)
- `secretRef` (`SecretReference`): Reference to an external secret manager entry (mutually exclusive with inlineSecret)
- `headerName` (`String`): Desired HTTP header to carry the credential (defaults to Authorization)
- `prefix` (`String`): Optional prefix prepended to the secret (e.g., "Bearer ")

[Java](../../java.md)

Related types — open only those used by your request:

- [SecretReference](SecretReference.md)
