<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# GoodMem TypeScript SDK

[Published package 0.1.6](https://registry.npmjs.org/@pairsystems/goodmem/0.1.6); server guidance assumes GoodMem 1.0.320 or later.

Install `npm install @pairsystems/goodmem@0.1.6` (Node 20+). Import `Goodmem`
(also exported as `Client`), then construct it with `new Goodmem({ baseUrl, apiKey })`
using environment/configuration values. See `GoodmemConfig` for other options.

Methods take typed bodies and optional `RequestOptions` (`signal`, `timeoutMs`,
`headers`). `Promise<Page<T>>` results expose `page.items` for the current page;
async iteration follows cursors, including `apikeys.list`. Retrieval returns an
`AsyncIterable` of events. Preserve passages alongside nonfatal status events.

Request types are exported by the package. Model pages preserve inheritance,
unions, and credential-specific overload constraints. `?` permits omission;
`null` is allowed only where listed. Follow a nested type link only when using it.

Errors include `APIError` (`statusCode`), `NetworkError`, and `ParseError`.
Never log raw provider error bodies or keys.

## Examples

- [Ingest retrieve](typescript/examples/ingest-retrieve.md)
- [Issue scoped key](typescript/examples/issue-scoped-key.md)
- [List spaces](typescript/examples/list-spaces.md)
- [Register embedder](typescript/examples/register-embedder.md)

## Namespaces

Open one index, then the needed operation and models. Search for a symbol inside this language directory when search is available; avoid reading whole directories.

- [accessPolicy](typescript/accessPolicy.md)
- [admin](typescript/admin.md)
- [apikeys](typescript/apikeys.md)
- [embedders](typescript/embedders.md)
- [instance](typescript/instance.md)
- [llms](typescript/llms.md)
- [memories](typescript/memories.md)
- [ocr](typescript/ocr.md)
- [ping](typescript/ping.md)
- [rerankers](typescript/rerankers.md)
- [serviceIdentities](typescript/serviceIdentities.md)
- [spaces](typescript/spaces.md)
- [system](typescript/system.md)
- [userEnrollments](typescript/userEnrollments.md)
- [users](typescript/users.md)

[SDK rules](../SKILL.md)

Related types — open only those used by your request:

- [GoodmemConfig](typescript/models/GoodmemConfig.md)
- [RequestOptions](typescript/models/RequestOptions.md)
