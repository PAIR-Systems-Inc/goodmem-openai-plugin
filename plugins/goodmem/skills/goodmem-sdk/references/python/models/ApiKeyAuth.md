<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# ApiKeyAuth

Configuration for classic API-key authentication.

- `inline_secret` (`str | None`, optional): Secret stored directly in GoodMem (mutually exclusive with secret_ref) JSON: `inlineSecret`.
- `secret_ref` (`SecretReference | None`, optional): Reference to an external secret manager entry (mutually exclusive with inline_secret) JSON: `secretRef`.
- `header_name` (`str | None`, optional): Desired HTTP header to carry the credential (defaults to Authorization) JSON: `headerName`.
- `prefix` (`str | None`, optional): Optional prefix prepended to the secret (e.g., "Bearer ")

[Python](../../python.md)

Related types — open only those used by your request:

- [SecretReference](SecretReference.md)
