<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LlmsListOptions

- `ownerId` (`string`, optional): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-LLM READ_LLM filtering.
- `providerType` (`LLMProviderType`, optional): Filter LLMs by provider type. Allowed values match the LLMProviderType schema.
- `label` (`Record<string, string>`, optional): Filter by label key-value pairs. Label filters accept either label.<key>=<value> or label[key]=value (for example, label.environment=production or label[environment]=production).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [LLMProviderType](LLMProviderType.md)
