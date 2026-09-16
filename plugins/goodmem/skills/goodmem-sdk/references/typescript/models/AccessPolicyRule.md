<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AccessPolicyRule

One operation, selector, and optional assigned resource.

- `operation` (`Operation`, required): Protected operation.
- `selector` (`Selector`, required): Resource-selection semantics.
- `assignedResource` (`AccessPolicyTarget | null`, optional): Required exactly for EXACT and DIRECT_MEMBERS_OF selectors.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AccessPolicyTarget](AccessPolicyTarget.md)
- [Operation](Operation.md)
- [Selector](Selector.md)
