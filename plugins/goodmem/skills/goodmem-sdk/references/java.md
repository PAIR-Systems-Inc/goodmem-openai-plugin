<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# GoodMem Java SDK

[Published package 0.2.2](https://repo.maven.apache.org/maven2/ai/pairsys/goodmem-java/0.2.2/goodmem-java-0.2.2-sources.jar); server guidance assumes GoodMem 1.0.320 or later.

Use `ai.pairsys:goodmem-java:0.2.2` with JDK 21+. Construct `Goodmem` with
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

## Examples

- [Ingest retrieve](java/examples/ingest-retrieve.md)
- [Issue scoped key](java/examples/issue-scoped-key.md)
- [Register embedder](java/examples/register-embedder.md)

## Namespaces

Open one index, then the needed operation and models. Search for a symbol inside this language directory when search is available; avoid reading whole directories.

- [accessPolicy](java/accessPolicy.md)
- [admin](java/admin.md)
- [apikeys](java/apikeys.md)
- [embedders](java/embedders.md)
- [instance](java/instance.md)
- [llms](java/llms.md)
- [memories](java/memories.md)
- [ocr](java/ocr.md)
- [ping](java/ping.md)
- [rerankers](java/rerankers.md)
- [serviceIdentities](java/serviceIdentities.md)
- [spaces](java/spaces.md)
- [system](java/system.md)
- [userEnrollments](java/userEnrollments.md)
- [users](java/users.md)

[SDK rules](../SKILL.md)
