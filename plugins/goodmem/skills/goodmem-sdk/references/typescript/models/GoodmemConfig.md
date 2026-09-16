<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# GoodmemConfig

- `baseUrl` (`string`, required):
- `apiKey` (`string | null`, optional):
- `headers` (`HeadersInit`, optional):
- `fetch` (`typeof fetch`, optional):
- `timeoutMs` (`number`, optional): Default request timeout in milliseconds. Per-request timeoutMs overrides
this value; set a per-request timeoutMs of 0 to disable the default.
- `maxStreamLineBytes` (`number`, optional): Maximum bytes allowed for one NDJSON stream line. Defaults to 8 MiB.

[TypeScript](../../typescript.md)
