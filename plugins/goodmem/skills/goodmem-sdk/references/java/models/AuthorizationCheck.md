<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# AuthorizationCheck

One concrete, advisory authorization check. Top-level creates and LIST_API_KEY target INSTANCE; CREATE_MEMORY and LIST_MEMORY target a parent SPACE; ordinary resource operations target the concrete resource. LIST_RETRIEVE_MEMORY_LOG_POLICY is not supported by this endpoint.

- `operation` (`Operation`): Operation the caller proposes to perform.
- `target` (`AccessPolicyTarget`): Target required by the operation: INSTANCE for top-level creates and LIST_API_KEY; parent SPACE for CREATE_MEMORY or LIST_MEMORY; otherwise the concrete resource.

[Java](../../java.md)

Related types — open only those used by your request:

- [AccessPolicyTarget](AccessPolicyTarget.md)
- [Operation](Operation.md)
