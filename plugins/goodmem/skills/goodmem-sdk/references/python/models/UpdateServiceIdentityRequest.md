<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateServiceIdentityRequest

Updates explicitly present profile fields. Empty description clears it; omitted fields remain unchanged. Ownership is changed only through the transfer endpoint.

- `display_name` (`str | None`, optional): Replacement display name. A present blank value is invalid. JSON: `displayName`.
- `description` (`str | None`, optional): Replacement description. An empty string clears the description.
- `replace_labels` (`dict[str, str] | None`, optional): Complete replacement label map; an empty map clears all labels and is mutually exclusive with merge_labels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Labels to upsert; must contain at least one entry and is mutually exclusive with replace_labels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.

[Python](../../python.md)
