<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LLMSamplingParams

Sampling and generation parameters for controlling LLM text output

- `maxTokens` (`Integer`): Maximum tokens to generate (>0 if set; provider-dependent limits apply)
- `temperature` (`Double`): Sampling temperature; valid range depends on the configured provider
- `topP` (`Double`): Nucleus sampling threshold 0.0-1.0 (smaller values focus on higher probability tokens)
- `topK` (`Integer`): Top-k sampling limit (>0 if set; primarily for local/open-source models)
- `frequencyPenalty` (`Double`): Frequency penalty; valid range depends on the configured provider
- `presencePenalty` (`Double`): Presence penalty; valid range depends on the configured provider
- `stopSequences` (`java.util.List<String>`): Generation stop sequences; generation halts on exact match

[Java](../../java.md)
