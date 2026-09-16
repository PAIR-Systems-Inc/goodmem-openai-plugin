Install `npm install @pairsystems/goodmem@@VERSION@` (Node 20+). Import `Goodmem`
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
