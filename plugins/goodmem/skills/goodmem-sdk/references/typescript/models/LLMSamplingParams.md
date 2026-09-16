<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMSamplingParams

Sampling and generation parameters for controlling LLM text output

- `maxTokens` (`number | null`, optional): Maximum tokens to generate (>0 if set; provider-dependent limits apply)
- `temperature` (`number | null`, optional): Sampling temperature; valid range depends on the configured provider
- `topP` (`number | null`, optional): Nucleus sampling threshold 0.0-1.0 (smaller values focus on higher probability tokens)
- `topK` (`number | null`, optional): Top-k sampling limit (>0 if set; primarily for local/open-source models)
- `frequencyPenalty` (`number | null`, optional): Frequency penalty; valid range depends on the configured provider
- `presencePenalty` (`number | null`, optional): Presence penalty; valid range depends on the configured provider
- `stopSequences` (`Array<string> | null`, optional): Generation stop sequences; generation halts on exact match

[TypeScript](../../typescript.md)
