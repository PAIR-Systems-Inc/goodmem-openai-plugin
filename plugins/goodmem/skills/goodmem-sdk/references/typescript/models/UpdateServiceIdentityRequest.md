<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateServiceIdentityRequest

Updates explicitly present profile fields. Empty description clears it; omitted fields remain unchanged. Ownership is changed only through the transfer endpoint.

- `displayName` (`string | null`, optional): Replacement display name. A present blank value is invalid.
- `description` (`string | null`, optional): Replacement description. An empty string clears the description.
- `replaceLabels` (`Record<string, string> | null`, optional): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`Record<string, string> | null`, optional): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[TypeScript](../../typescript.md)
