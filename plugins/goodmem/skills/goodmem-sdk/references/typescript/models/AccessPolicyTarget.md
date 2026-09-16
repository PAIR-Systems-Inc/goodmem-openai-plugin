<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AccessPolicyTarget

A typed access-policy target. resourceId is omitted for INSTANCE and required otherwise.

- `kind` (`ResourceKind`, required): Concrete target kind.
- `resourceId` (`string | null`, optional): Concrete resource UUID; omitted for the singleton INSTANCE target.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ResourceKind](ResourceKind.md)
