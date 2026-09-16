<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# AccessPolicyRule

One operation, selector, and optional assigned resource.

- `operation` (`Operation | None`, required): Protected operation.
- `selector` (`Selector | None`, required): Resource-selection semantics.
- `assigned_resource` (`AccessPolicyTarget | None`, optional): Required exactly for EXACT and DIRECT_MEMBERS_OF selectors. JSON: `assignedResource`.

[Python](../../python.md)

Related types — open only those used by your request:

- [AccessPolicyTarget](AccessPolicyTarget.md)
- [Operation](Operation.md)
- [Selector](Selector.md)
