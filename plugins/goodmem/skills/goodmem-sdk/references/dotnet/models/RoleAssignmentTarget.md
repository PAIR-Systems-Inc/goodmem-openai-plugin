<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RoleAssignmentTarget

An INSTANCE or SPACE role-assignment boundary. resourceId is omitted for INSTANCE and required for SPACE.

`Goodmem.Client.Models.RoleAssignmentTarget`

- `Kind` (`string`, required): Role-assignment target kind. JSON: `kind`.
- `ResourceId` (`string?`): Memory-space UUID; omitted for the singleton INSTANCE target. JSON: `resourceId`.

[.NET](../../dotnet.md)
