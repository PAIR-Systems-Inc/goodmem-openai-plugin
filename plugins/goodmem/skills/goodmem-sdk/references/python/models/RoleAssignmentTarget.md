<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# RoleAssignmentTarget

An INSTANCE or SPACE role-assignment boundary. resourceId is omitted for INSTANCE and required for SPACE.

- `kind` (`Literal['INSTANCE', 'SPACE'] | None`, required): Role-assignment target kind.
- `resource_id` (`str | None`, optional): Memory-space UUID; omitted for the singleton INSTANCE target. JSON: `resourceId`.

[Python](../../python.md)
