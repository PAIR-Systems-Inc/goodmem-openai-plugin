<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# AccessPolicyTarget

A typed access-policy target. resourceId is omitted for INSTANCE and required otherwise.

- `kind` (`ResourceKind | None`, required): Concrete target kind.
- `resource_id` (`str | None`, optional): Concrete resource UUID; omitted for the singleton INSTANCE target. JSON: `resourceId`.

[Python](../../python.md)

Related types — open only those used by your request:

- [ResourceKind](ResourceKind.md)
