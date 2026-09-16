<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AuthorizationCheck

One concrete, advisory authorization check. Top-level creates and LIST_API_KEY target INSTANCE; CREATE_MEMORY and LIST_MEMORY target a parent SPACE; ordinary resource operations target the concrete resource. LIST_RETRIEVE_MEMORY_LOG_POLICY is not supported by this endpoint.

`Goodmem.Client.Models.AuthorizationCheck`

- `Operation` (`Operation`, required): Operation the caller proposes to perform. JSON: `operation`.
- `Target` (`AccessPolicyTarget`, required): Target required by the operation: INSTANCE for top-level creates and LIST_API_KEY; parent SPACE for CREATE_MEMORY or LIST_MEMORY; otherwise the concrete resource. JSON: `target`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [AccessPolicyTarget](AccessPolicyTarget.md)
- [Operation](Operation.md)
