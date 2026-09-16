# GoodMem TypeScript SDK

Install `npm install @pairsystems/goodmem@@VERSION@` (Node 20+).

```ts
import { Goodmem } from "@pairsystems/goodmem";

const baseUrl = process.env.GOODMEM_BASE_URL;
if (!baseUrl) throw new Error("GOODMEM_BASE_URL is required");
const client = new Goodmem({ baseUrl, apiKey: process.env.GOODMEM_API_KEY });
for await (const space of await client.spaces.list()) {
  console.log(space.spaceId, space.name);
}
```

`Goodmem` is also exported as `Client`. Methods take typed request/option
objects and optional trailing `RequestOptions` (`signal`, `timeoutMs`, `headers`).
Paginated methods, including `apikeys.list`, return `Promise<Page<T>>`:
`page.items` is the current page; async iteration follows all cursors.
`memories.retrieve(message, { spaceIds })` returns an `AsyncIterable` of events.
Check `event.status` as well as chunks; a synthesis warning does not invalidate
usable passages. Await COMPLETED with a deadline before retrieving new memories;
stop on FAILED. See the Python example in [the SDK skill](../SKILL.md) for the flow.

Request and response shapes are exported from the package. Use their declarations
when constructing nested bodies; `publicRead` is absent from space creation.
Grant access through access policies. Errors include `APIError` (`statusCode`),
`NetworkError`, and `ParseError`; never log raw provider error bodies or keys.
