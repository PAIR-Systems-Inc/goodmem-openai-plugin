---
name: save-conversation
description: Save a useful conversation to GoodMem as self-contained question-and-answer pairs, including documents shared in the conversation. Use only when the user asks to save, remember, or keep the discussion.
---

# Save a conversation

Save only when the user asks. Capture durable decisions, facts, and conclusions;
omit greetings, clarifying one-liners, and tool-call chatter.

## Choose the space

Call `goodmem_spaces_list` first. Reuse an obviously matching space or create one
named for the topic, not the date. If the user supplies a name, use it exactly.
Tell the user which space you chose. Keep using that space if they save more of
the same session later.

## Save self-contained exchanges

Create one memory per useful exchange with both sides present:

```text
Q: What did we decide about the vendor contract?
A: We chose Cooperativa San Rafael at 6.80 USD/kg, quarterly shipments,
   pending legal review of the termination clause.
```

Call `goodmem_memories_create` once per pair with metadata such as
`{"type":"qa_pair","topic":"vendor contract"}`. Never save a bare answer that
will lose its meaning outside the current chat.

## Include shared documents

A document discussed in the saved conversation is part of what the user asked to
keep. Follow `work-with-documents` to save its readable content, not merely its
filename or path. Use metadata connecting it to the conversation, and name the
document in the related Q&A answer so later retrieval connects them.

If a document is illegible, say so and save the useful discussion rather than
silently omitting everything.

## Confirm the result

Report the space name, number of Q&A pairs, and documents saved. If processing is
still underway, distinguish "saved" from "searchable" and follow the processing
rules in `using-goodmem-memory`.

Confirm the specific memory before deletion. Never bulk-delete unless the user
explicitly covers the whole set.
