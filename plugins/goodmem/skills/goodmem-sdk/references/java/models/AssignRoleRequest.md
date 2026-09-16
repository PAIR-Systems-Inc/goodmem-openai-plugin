<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# AssignRoleRequest

Assigns one code-defined role at an INSTANCE or SPACE boundary.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `roleAssignmentId` (`RoleAssignmentId`): Optional caller-provided role-assignment UUID. Typed wrapper `RoleAssignmentId`; build from a raw string with `RoleAssignmentId.from(String)`.
- `principalId` (`PrincipalId`): Active principal receiving the role. Typed wrapper `PrincipalId`; build from a raw string with `PrincipalId.from(String)`.
- `role` (`AssignRoleRequestRole`): Code-defined non-ROOT role to assign. Typed enum `AssignRoleRequestRole`; unknown server values fail Jackson deserialization loudly.
- `assignedResource` (`RoleAssignmentTarget`): INSTANCE or SPACE boundary receiving the assignment.

[Java](../../java.md)

Related types — open only those used by your request:

- [AssignRoleRequestRole](AssignRoleRequestRole.md)
- [PrincipalId](PrincipalId.md)
- [RoleAssignmentId](RoleAssignmentId.md)
- [RoleAssignmentTarget](RoleAssignmentTarget.md)
