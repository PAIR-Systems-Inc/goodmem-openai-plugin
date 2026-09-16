<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AccessPolicyRule

One operation, selector, and optional assigned resource.

`Goodmem.Client.Models.AccessPolicyRule`

- `AssignedResource` (`AccessPolicyTarget?`): Required exactly for EXACT and DIRECT_MEMBERS_OF selectors. JSON: `assignedResource`.
- `Operation` (`Operation`, required): Protected operation. JSON: `operation`.
- `Selector` (`Selector`, required): Resource-selection semantics. JSON: `selector`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [AccessPolicyTarget](AccessPolicyTarget.md)
- [Operation](Operation.md)
- [Selector](Selector.md)
