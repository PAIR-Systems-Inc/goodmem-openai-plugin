<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# LLMSamplingParams

Sampling and generation parameters for controlling LLM text output

```python
from goodmem.models import LLMSamplingParams
```

- `max_tokens` (`int | None`, optional): Maximum tokens to generate (>0 if set; provider-dependent limits apply) JSON: `maxTokens`.
- `temperature` (`float | None`, optional): Sampling temperature; valid range depends on the configured provider
- `top_p` (`float | None`, optional): Nucleus sampling threshold 0.0-1.0 (smaller values focus on higher probability tokens) JSON: `topP`.
- `top_k` (`int | None`, optional): Top-k sampling limit (>0 if set; primarily for local/open-source models) JSON: `topK`.
- `frequency_penalty` (`float | None`, optional): Frequency penalty; valid range depends on the configured provider JSON: `frequencyPenalty`.
- `presence_penalty` (`float | None`, optional): Presence penalty; valid range depends on the configured provider JSON: `presencePenalty`.
- `stop_sequences` (`list[str] | None`, optional): Generation stop sequences; generation halts on exact match JSON: `stopSequences`.

[Python](../../python.md)
