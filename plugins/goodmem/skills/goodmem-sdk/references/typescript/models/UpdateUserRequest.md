<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateUserRequest

Updates explicitly present profile fields. Empty username or displayName clears that optional field; an omitted field remains unchanged.

- `email` (`string | null`, optional): Replacement email. A present empty value is invalid.
- `username` (`string | null`, optional): Replacement username. An empty string clears the username.
- `displayName` (`string | null`, optional): Replacement display name. An empty string clears the display name.
- `replaceLabels` (`Record<string, string> | null`, optional): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`Record<string, string> | null`, optional): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[TypeScript](../../typescript.md)
