<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# TransferOwnershipRequest

Names the principal that will become the resource owner.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `newOwnerId` (`NewOwnerId`): Existing principal UUID that will become the new owner. Typed wrapper `NewOwnerId`; build from a raw string with `NewOwnerId.from(String)`.

[Java](../../java.md)

Related types — open only those used by your request:

- [NewOwnerId](NewOwnerId.md)
