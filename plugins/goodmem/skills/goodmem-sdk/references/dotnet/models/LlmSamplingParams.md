<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# LlmSamplingParams

Sampling and generation parameters for controlling LLM text output

`Goodmem.Client.Models.LlmSamplingParams`

- `FrequencyPenalty` (`double?`): Frequency penalty; valid range depends on the configured provider JSON: `frequencyPenalty`.
- `MaxTokens` (`int?`): Maximum tokens to generate (>0 if set; provider-dependent limits apply) JSON: `maxTokens`.
- `PresencePenalty` (`double?`): Presence penalty; valid range depends on the configured provider JSON: `presencePenalty`.
- `StopSequences` (`IReadOnlyList<string>?`): Generation stop sequences; generation halts on exact match JSON: `stopSequences`.
- `Temperature` (`double?`): Sampling temperature; valid range depends on the configured provider JSON: `temperature`.
- `TopK` (`int?`): Top-k sampling limit (>0 if set; primarily for local/open-source models) JSON: `topK`.
- `TopP` (`double?`): Nucleus sampling threshold 0.0-1.0 (smaller values focus on higher probability tokens) JSON: `topP`.

[.NET](../../dotnet.md)
