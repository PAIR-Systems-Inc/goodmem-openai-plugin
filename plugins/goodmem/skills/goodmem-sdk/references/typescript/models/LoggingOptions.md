<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LoggingOptions

- `enabled` (`boolean | null`, optional): Opts this request in to durable server-side request logging. False or omitted does not opt out of admin policy logging.
- `callerAttributes` (`Record<string, unknown> | null`, optional): Optional flat scalar attributes attached if this request is persisted by caller opt-in or admin policy logging. Supported value types are string, integer, floating-point, and boolean. At most 32 entries are accepted.

[TypeScript](../../typescript.md)
