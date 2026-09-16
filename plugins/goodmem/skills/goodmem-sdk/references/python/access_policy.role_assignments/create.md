<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# access_policy.role_assignments.create

Assign a scoped role

Assigns one code-defined role to an active principal at INSTANCE or SPACE scope after requiring MANAGE_ACCESS. ROOT is maintained only by ownership workflows.

Args:
    role_assignment_id (str, optional): Optional caller-provided role-assignment UUID.
    principal_id (str): Active principal receiving the role.
    role (str): Code-defined non-ROOT role to assign.
    assigned_resource (RoleAssignmentTarget): INSTANCE or SPACE boundary receiving the assignment.

Returns:
    RoleAssignment

```python
access_policy.role_assignments.create(*, principal_id: 'str', role: 'str', assigned_resource: 'RoleAssignmentTarget', role_assignment_id: 'str | None' = None) -> 'RoleAssignment'
```

[access_policy.role_assignments](../access_policy.role_assignments.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [RoleAssignmentTarget](../models/RoleAssignmentTarget.md)
