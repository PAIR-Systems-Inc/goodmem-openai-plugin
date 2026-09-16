<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# PostProcessor

Post-processor configuration for transforming retrieval results. Custom processors are discovered from installed extensions and must be referenced by their fully qualified factory class name. See https://docs.goodmem.ai/docs/reference/post-processors/chat-post-processor/ for the built-in ChatPostProcessor configuration.

`Goodmem.Client.Models.PostProcessor`

- `Config` (`IReadOnlyDictionary<string, object>?`): Configuration parameters for the post-processor. Fields depend on the selected processor; see the linked documentation for the built-in ChatPostProcessor schema. JSON: `config`.
- `Name` (`string`, required): Fully qualified factory class name of the post-processor to apply. JSON: `name`.

[.NET](../../dotnet.md)
