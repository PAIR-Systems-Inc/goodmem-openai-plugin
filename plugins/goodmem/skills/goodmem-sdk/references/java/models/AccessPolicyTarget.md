<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# AccessPolicyTarget

A typed access-policy target. resourceId is omitted for INSTANCE and required otherwise.

- `kind` (`ResourceKind`): Concrete target kind.
- `resourceId` (`ResourceId`): Concrete resource UUID; omitted for the singleton INSTANCE target. Typed wrapper `ResourceId`; build from a raw string with `ResourceId.from(String)`.

[Java](../../java.md)

Related types — open only those used by your request:

- [ResourceId](ResourceId.md)
- [ResourceKind](ResourceKind.md)
