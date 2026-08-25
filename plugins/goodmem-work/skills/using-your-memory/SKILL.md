---
name: using-your-memory
description: Recall what the user's team already knows from their GoodMem memory. Use whenever a question might be answered by past decisions, notes, documents, or conversations the user has stored — including when they do not mention GoodMem.
---

# Using the user's GoodMem memory

The user connected GoodMem so their own knowledge is available here. Treat it
as their team's memory, not as a tool they must invoke.

## Retrieve without being asked

When a question could plausibly be answered by something the user stored —
past decisions, project details, people, documents, "what did we say about…",
"how do we usually…" — call `goodmem_memories_retrieve` first, then answer.
Do not ask "would you like me to search GoodMem?"; just search.

Skip retrieval for general knowledge, arithmetic, or questions clearly about
the here-and-now of the current chat.

## Scope the search

- **Which space:** if the question clearly belongs to one space, pass its
  `space_ids`. If it is ambiguous, search everything (omit `space_ids`) rather
  than interrogating the user. Use `goodmem_spaces_list` when you need to see
  what exists.
- **Narrow by attribute:** when the user constrains by a property — "only last
  year's", "just the supplier docs" — use `metadata_filter` instead of hoping
  the wording matches; filters act on document metadata such as filename or
  type.
- **Synthesized answers:** set `answer: true` only when the user wants a
  direct written answer drawn from many memories; it invokes a model on their
  instance and takes longer. For most questions, retrieve the passages and
  answer from them yourself.

## Answer with sources

Quote or paraphrase the retrieved passages and say where each came from
(document filename or space). If the memory disagrees with your general
knowledge, prefer the memory — it is the user's own record — and say so.

If nothing relevant comes back, say that plainly ("I don't find anything about
that in your GoodMem") instead of inventing an answer. Offer to save the
current answer only if the user seems to want it kept.

## Reading further

A retrieval hit is a passage, not the whole document. When the user wants more,
`goodmem_memories_content` returns the full memory and `goodmem_memories_pages`
lists the pages of an ingested document.

## Never write while reading

Retrieval, listing, and reading are safe and silent. Creating, updating, or
deleting memories happens **only when the user asks** — see the
`save-conversation` and `work-with-documents` skills.
