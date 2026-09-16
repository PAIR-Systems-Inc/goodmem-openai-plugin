<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateSpaceRequest

Request parameters for updating a space.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `name` (`String`): The new name for the space.
- `replaceLabels` (`java.util.Map<String, String>`): Labels to replace all existing labels. Mutually exclusive with mergeLabels.
- `mergeLabels` (`java.util.Map<String, String>`): Labels to merge with existing labels. Mutually exclusive with replaceLabels.

[Java](../../java.md)
