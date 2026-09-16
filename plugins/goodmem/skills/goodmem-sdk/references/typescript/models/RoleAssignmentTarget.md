<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RoleAssignmentTarget

An INSTANCE or SPACE role-assignment boundary. resourceId is omitted for INSTANCE and required for SPACE.

- `kind` (`"INSTANCE" | "SPACE"`, required): Role-assignment target kind.
- `resourceId` (`string | null`, optional): Memory-space UUID; omitted for the singleton INSTANCE target.

[TypeScript](../../typescript.md)
