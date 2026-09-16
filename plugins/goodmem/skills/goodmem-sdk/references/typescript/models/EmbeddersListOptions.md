<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# EmbeddersListOptions

- `ownerId` (`string`, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-embedder READ_EMBEDDER filtering.
- `providerType` (`ProviderType`, optional): Filter embedders by provider type. Allowed values match the ProviderType schema.
- `label` (`Record<string, string>`, optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [ProviderType](ProviderType.md)
