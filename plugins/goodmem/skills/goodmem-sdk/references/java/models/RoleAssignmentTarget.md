<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RoleAssignmentTarget

An INSTANCE or SPACE role-assignment boundary. resourceId is omitted for INSTANCE and required for SPACE.

- `kind` (`RoleAssignmentTargetKind`): Role-assignment target kind. Typed enum `RoleAssignmentTargetKind`; unknown server values fail Jackson deserialization loudly.
- `resourceId` (`ResourceId`): Memory-space UUID; omitted for the singleton INSTANCE target. Typed wrapper `ResourceId`; build from a raw string with `ResourceId.from(String)`.

[Java](../../java.md)

Related types — open only those used by your request:

- [ResourceId](ResourceId.md)
- [RoleAssignmentTargetKind](RoleAssignmentTargetKind.md)
