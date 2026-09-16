<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ResourceId

Typed handle for a resource id (UUID).

Wire format is the bare id string (typically a UUID), so ResourceId is
 drop-in compatible with the `String`-typed id fields on the
 server. Prefer this over a bare `String` so the compiler
 catches cross-resource mixups (passing a `MemoryId` where a
 `SpaceId` is expected).

The backing field is `String` (not `UUID`) so test
 fixtures and dev environments using non-UUID identifiers still work.
 Production ids are UUIDs by server contract; call `asUuid()`
 when you need the parsed form.

- `value` (`String`):

[Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](MemoryId.md)
- [SpaceId](SpaceId.md)
