# GoodMem

Persistent memory for your AI workflows — store knowledge in access-controlled
spaces on your own [GoodMem](https://docs.goodmem.ai) instance, and retrieve it
with semantic search, reranking, and document ingestion.

## What you can do

- **Create spaces** to hold related memories — one per project, team, or topic.
- **Add memories** from plain text, or ingest whole documents (PDF, DOCX;
  scanned-file OCR is available on GoodMem Enterprise).
- **Search semantically** across your spaces, narrow results with metadata
  filters, and rerank for precision.
- **Ask direct questions** and let an LLM summarize the retrieved memories into
  an answer with sources.
- **Tune retrieval** by choosing the embedding models, rerankers, and LLMs that
  fit your data.

## Requirements

- A running **GoodMem instance** — [install guide](https://docs.goodmem.ai)
  (self-hosted, one command) or your organization's existing server.
- A **GoodMem API key** (`gm_…`) — from your GoodMem Console, or ask your
  administrator.
- **Node.js 18+** — the bundled MCP server runs via `npx`.

## Installation

From the plugin directory (once listed): open `/plugins` in Codex and install
**GoodMem**.

Directly from this repository:

```bash
codex plugin marketplace add PAIR-Systems-Inc/goodmem-openai-plugin
codex plugin install goodmem
```

## Configuration

The plugin connects to your instance through two environment variables:

| Variable | Required | Description |
|---|---|---|
| `GOODMEM_BASE_URL` | yes | Your instance's REST URL, e.g. `http://localhost:8081` or `https://goodmem.example.com` |
| `GOODMEM_API_KEY` | yes | Your API key (`gm_…`) |
| `NODE_EXTRA_CA_CERTS` | only for private CAs | Absolute path to your CA certificate file, if your server uses one |

Set them in your shell profile (or your environment manager of choice):

```bash
export GOODMEM_BASE_URL="http://localhost:8081"
export GOODMEM_API_KEY="gm_your_key_here"
```

Works with every deployment type:

- **Local instance** — `GOODMEM_BASE_URL=http://localhost:8081`. The MCP server
  runs on your machine, so localhost works out of the box.
- **Self-hosted server** — point `GOODMEM_BASE_URL` at your server's HTTPS URL.
  If it uses a certificate from your organization's private CA, set
  `NODE_EXTRA_CA_CERTS` to the CA file path.
- **GoodMem cloud** — use your workspace URL and API key from the Console.

## Quick start

Try these once installed:

- *"Set up a GoodMem space for this project and ingest the docs folder."*
- *"What do we already know about this topic in GoodMem?"*
- *"Save a summary of this session to GoodMem."*

## Skills

The plugin ships task-focused skills that guide the full workflow:

- **goodmem-help** — connection setup, configuration checks, and
  troubleshooting.
- **goodmem-memory-workflow** — the memory workflow end to end: create spaces,
  ingest, wait for processing, retrieve.
- **goodmem-sdk** — verified Python and Java SDK references for building
  GoodMem into your own applications.

## Tools

The bundled MCP server exposes the full GoodMem API as tools, organized by
namespace: `spaces` (create, list, update, get, delete), `memories` (create,
batch ingest, list, retrieve, content, pages, delete), `embedders` / `llms` /
`rerankers` (provision and manage retrieval models), `ocr` (document
ingestion, GoodMem Enterprise), plus system, user, and API-key management for
operators. Retrieval
tools are read-only; destructive operations are labeled as such and always
subject to your approval in Codex.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `401 Unauthorized` | Missing or invalid API key | Check `GOODMEM_API_KEY`; keys start with `gm_` |
| `ECONNREFUSED` / timeout on startup | Wrong URL or instance not running | Verify `GOODMEM_BASE_URL` (scheme, host, port) and that the instance is up |
| TLS certificate error | Server uses a private CA | Set `NODE_EXTRA_CA_CERTS` to your CA certificate file |
| OCR ingestion fails while other tools work | OCR requires GoodMem Enterprise | Ingest the document as text instead, or ask your administrator about GoodMem Enterprise |
| Retrieval times out | Answer summarization on large spaces can run long | Retry, lower the result limit, or ask without summarization |

## Support

- Documentation: [docs.goodmem.ai](https://docs.goodmem.ai)
- Contact: [support@pairsys.ai](mailto:support@pairsys.ai)
- License: [MIT](../../LICENSE)
