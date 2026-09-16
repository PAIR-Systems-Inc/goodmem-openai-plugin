<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AccessPolicyTarget

A typed access-policy target. resourceId is omitted for INSTANCE and required otherwise.

`Goodmem.Client.Models.AccessPolicyTarget`

- `Kind` (`ResourceKind`, required): Concrete target kind. JSON: `kind`.
- `ResourceId` (`string?`): Concrete resource UUID; omitted for the singleton INSTANCE target. JSON: `resourceId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [ResourceKind](ResourceKind.md)
