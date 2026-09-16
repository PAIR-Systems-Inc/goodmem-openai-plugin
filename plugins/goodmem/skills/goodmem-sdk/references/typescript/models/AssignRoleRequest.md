<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AssignRoleRequest

Assigns one code-defined role at an INSTANCE or SPACE boundary.

- `roleAssignmentId` (`string | null`, optional): Optional caller-provided role-assignment UUID.
- `principalId` (`string`, required): Active principal receiving the role.
- `role` (`"ADMIN" | "USER" | "SPACE_VIEWER" | "SPACE_CONTRIBUTOR" | "SPACE_CONTENT_MANAGER" | "SPACE_ADMIN"`, required): Code-defined non-ROOT role to assign.
- `assignedResource` (`RoleAssignmentTarget`, required): INSTANCE or SPACE boundary receiving the assignment.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RoleAssignmentTarget](RoleAssignmentTarget.md)
