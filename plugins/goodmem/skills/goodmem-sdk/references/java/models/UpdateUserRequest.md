<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateUserRequest

Updates explicitly present profile fields. Empty username or displayName clears that optional field; an omitted field remains unchanged.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `email` (`String`): Replacement email. A present empty value is invalid.
- `username` (`String`): Replacement username. An empty string clears the username.
- `displayName` (`String`): Replacement display name. An empty string clears the display name.
- `replaceLabels` (`java.util.Map<String, String>`): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`java.util.Map<String, String>`): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[Java](../../java.md)
