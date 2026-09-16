<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# UpdateApiKeyRequestBase

- `status` (`"ACTIVE" | "INACTIVE" | null`, optional): New status for the API key. INACTIVE is permanent; revoked keys cannot be reactivated.
- `replaceLabels` (`Record<string, string> | null`, optional): Replace all existing labels with this set. Mutually exclusive with mergeLabels. The stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`Record<string, string> | null`, optional): Merge these labels with existing ones. Mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[TypeScript](../../typescript.md)
