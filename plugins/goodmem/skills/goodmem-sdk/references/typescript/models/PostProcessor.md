<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# PostProcessor

Post-processor configuration for transforming retrieval results. Custom processors are discovered from installed extensions and must be referenced by their fully qualified factory class name. See https://docs.goodmem.ai/docs/reference/post-processors/chat-post-processor/ for the built-in ChatPostProcessor configuration.

- `name` (`string`, required): Fully qualified factory class name of the post-processor to apply.
- `config` (`Record<string, unknown> | null`, optional): Configuration parameters for the post-processor. Fields depend on the selected processor; see the linked documentation for the built-in ChatPostProcessor schema.

[TypeScript](../../typescript.md)
