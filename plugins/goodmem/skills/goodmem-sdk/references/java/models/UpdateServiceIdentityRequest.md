<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateServiceIdentityRequest

Updates explicitly present profile fields. Empty description clears it; omitted fields remain unchanged. Ownership is changed only through the transfer endpoint.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `displayName` (`String`): Replacement display name. A present blank value is invalid.
- `description` (`String`): Replacement description. An empty string clears the description.
- `replaceLabels` (`java.util.Map<String, String>`): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`java.util.Map<String, String>`): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[Java](../../java.md)
