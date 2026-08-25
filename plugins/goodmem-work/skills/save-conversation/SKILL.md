---
name: save-conversation
description: Save a chat session to GoodMem as question-and-answer pairs, including any documents that were shared. Use when the user asks to save, remember, or keep this conversation, this thread, or what was discussed.
---

# Saving a conversation to GoodMem

Save **only when the user asks.** Never store conversation content on your own
initiative. When they do ask, capture the session so it is useful months later:
each memory must make sense on its own, without the surrounding chat.

## 1. Choose the space

- Call `goodmem_spaces_list` first.
- Reuse an obviously matching space if one exists; otherwise create a new one
  with `goodmem_spaces_create` named after the topic ("vendor-negotiation-q3",
  "onboarding-notes"), not after the date.
- **Tell the user which space you chose** so they can correct it. If they name
  one ("call it last year data"), use their name exactly.

## 2. Save question-and-answer pairs — never a bare answer

One memory per exchange. Each memory contains **both the user's question and
your answer**, so the memory is self-contained:

```
Q: What did we decide about the vendor contract?
A: We chose Cooperativa San Rafael at 6.80 USD/kg, quarterly shipments,
   pending legal review of the termination clause.
```

Save the pairs with `goodmem_memories_create`, one call per memory — there
is no batch tool, by design. Attach metadata to every memory: `{"type": "qa_pair", "topic": "<short topic>"}`.

Do not save: greetings, clarifying one-liners, or your own tool-call chatter.
Save the exchanges that carry decisions, facts, or conclusions.

## 3. Documents shared in the conversation must be saved too

When the user uploaded or pasted a document (PDF, spreadsheet, notes) and asks
to save the conversation, **the document is part of what they are saving.**
For each document:

1. Save its content as its own memory — the extracted text you can already
   read, not a reference to a file the memory store cannot open.
2. Set metadata that ties it back to the conversation:
   `{"type": "document", "filename": "<original filename>", "context": "<the
   question or task the document was shared for>"}`.
3. If the document is long, save it as several memories split at natural
   section boundaries, each carrying the same filename metadata plus
   `{"part": "2 of 5"}`.
4. In the Q&A pair that discussed the document, name the document in the answer
   text ("…based on supplier-contract.pdf…") so a later search connects them.

If a document is a scanned image or an image-only PDF, read it yourself:
transcribe the text and describe any figures or photos in words, then save
those parts as memories. If a file is truly illegible, tell the user plainly
and save the conversation's discussion of it rather than silently skipping it.

## 4. Confirm, then keep going

Report what you saved: the space name, how many pairs, and which documents.
Keep the same space for the rest of the session — if the user asks again later
in the same conversation, append the new exchanges there rather than creating a
second space.

## 5. Deleting

If the user wants something removed, confirm the specific memory first, then
use `goodmem_memories_delete`. Never bulk-delete without an explicit
instruction covering the whole set.
