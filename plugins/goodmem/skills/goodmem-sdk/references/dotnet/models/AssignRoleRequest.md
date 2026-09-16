<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AssignRoleRequest

Assigns one code-defined role at an INSTANCE or SPACE boundary.

`Goodmem.Client.Models.AssignRoleRequest`

- `AssignedResource` (`RoleAssignmentTarget`, required): INSTANCE or SPACE boundary receiving the assignment. JSON: `assignedResource`.
- `PrincipalId` (`string`, required): Active principal receiving the role. JSON: `principalId`.
- `Role` (`string`, required): Code-defined non-ROOT role to assign. JSON: `role`.
- `RoleAssignmentId` (`string?`): Optional caller-provided role-assignment UUID. JSON: `roleAssignmentId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [RoleAssignmentTarget](RoleAssignmentTarget.md)
