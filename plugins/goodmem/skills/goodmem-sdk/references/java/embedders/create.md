<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# embedders.create

```java
EmbedderResponse create(EmbedderCreationRequest request)
```

Create a new embedder

Creates an embedder configuration for use with memory spaces. If ownerId is omitted, the authenticated principal becomes the owner; CREATE_EMBEDDER is evaluated against that proposed embedder and owner. Returns 409 when an equivalent embedder configuration already exists for the owner. See the [embedder provider guide](https://docs.goodmem.ai/docs/how-to/endpoint-registration) for provider-specific configuration.

```java
EmbedderResponse create(EmbedderCreationRequest request, String apiKey)
```

Convenience overload: auto-fills provider / endpoint / dimensionality
 from the bundled model registry keyed by `modelIdentifier`,
 and converts a bare `apiKey` string to the structured
 `EndpointAuthentication`. Pass `null` for
 `apiKey` to preserve `request.credentials()`.
 Any field already set on `request` wins over registry values.

[embedders](../embedders.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [EmbedderCreationRequest](../models/EmbedderCreationRequest.md)
