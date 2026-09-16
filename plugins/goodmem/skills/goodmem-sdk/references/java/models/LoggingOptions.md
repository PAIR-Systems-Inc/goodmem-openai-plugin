<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LoggingOptions

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `enabled` (`Boolean`): Opts this request in to durable server-side request logging. False or omitted does not opt out of admin policy logging.
- `callerAttributes` (`java.util.Map<String, Object>`): Optional flat scalar attributes attached if this request is persisted by caller opt-in or admin policy logging. Supported value types are string, integer, floating-point, and boolean. At most 32 entries are accepted.

[Java](../../java.md)
