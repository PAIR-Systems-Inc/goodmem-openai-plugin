Use `ai.pairsys:goodmem-java:@VERSION@` with JDK 21+. Construct `Goodmem` with
`Goodmem.builder().baseUrl(baseUrl).apiKey(apiKey).build()` and close it with
try-with-resources. `AsyncGoodmem` is also `AutoCloseable`; its methods return
`CompletableFuture<T>`. Read credentials from environment/configuration.

Models live in `ai.pairsys.goodmem.client.models`; options live in
`ai.pairsys.goodmem.client.api`. Prefer request builders to
canonical record constructors. Model pages list record components, field
constraints, and enum constants. Typed IDs provide `from(String)`; operation
pages retain String, UUID, and typed-ID overloads with their specific notes.

`Page<T>` iteration follows cursors, including `apikeys.list`. Retrieval returns
a closeable `RetrieveMemoryStream`. `ApiException` carries HTTP status; subclasses
include `NotFoundException` and `RateLimitException`. Preserve usable passages
when synthesis fails, and keep keys and provider error bodies out of logs.
