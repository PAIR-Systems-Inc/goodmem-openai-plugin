<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# UpdateUserRequest

Updates explicitly present profile fields. Empty username or displayName clears that optional field; an omitted field remains unchanged.

- `email` (`str | None`, optional): Replacement email. A present empty value is invalid.
- `username` (`str | None`, optional): Replacement username. An empty string clears the username.
- `display_name` (`str | None`, optional): Replacement display name. An empty string clears the display name. JSON: `displayName`.
- `replace_labels` (`dict[str, str] | None`, optional): Complete replacement label map; an empty map clears all labels and is mutually exclusive with merge_labels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.
- `merge_labels` (`dict[str, str] | None`, optional): Labels to upsert; must contain at least one entry and is mutually exclusive with replace_labels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.

[Python](../../python.md)
