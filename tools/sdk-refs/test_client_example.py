#!/usr/bin/env python3
"""Execute shipped examples through real SDK clients and a local HTTP fixture.

This checks request/response contracts, not a live GoodMem/provider deployment.
"""
import argparse
import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

SPACE = "00000000-0000-0000-0000-000000000001"
MEMORY = "00000000-0000-0000-0000-000000000002"
AUDIT = {"createdAt": 1, "updatedAt": 1, "createdById": SPACE, "updatedById": SPACE}


def run(language, scenario, command, cwd, failed=False):
    calls, errors = [], []
    polls, current = 0, "PENDING"

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def reply(self, data, content_type="application/json"):
            data = data.encode() if isinstance(data, str) else json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def memory(self):
            return {"memoryId": MEMORY, "spaceId": SPACE, "originalContentRef": "",
                    "contentType": "text/plain", "processingStatus": current,
                    "pageImageStatus": "UNSPECIFIED", "pageImageCount": 0, "metadata": {}, **AUDIT}

        def handle_request(self):
            nonlocal polls, current
            assert self.headers.get("x-api-key") == "gm_fake_fixture", "GoodMem authentication missing"
            path = urlsplit(self.path).path
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or "{}")
            calls.append((self.command, self.path, body))
            if scenario == "list-spaces" and self.command == "GET" and path == "/v1/spaces":
                query = parse_qs(urlsplit(self.path).query)
                cursor_name = "next_token" if language == "python" else "nextToken"
                final = query.get(cursor_name) == ["next"]
                self.reply({"spaces": [{
                    "spaceId": MEMORY if final else SPACE, "name": "second-page" if final else "first-page",
                    "ownerId": SPACE, "spaceEmbedders": [], "labels": {}, **AUDIT,
                }], **({} if final else {"nextToken": "next"})})
            elif scenario == "ingest-retrieve" and self.command == "GET" and path == f"/v1/memories/{MEMORY}":
                polls += 1
                current = "FAILED" if failed else ("COMPLETED" if polls >= 2 else "PROCESSING")
                self.reply(self.memory())
            elif scenario == "ingest-retrieve" and self.command == "POST" and path == "/v1/memories":
                assert body["spaceId"] == SPACE and body["originalContent"] == "GoodMem stores and retrieves memories."
                assert body["contentType"] == "text/plain"
                self.reply(self.memory())
            elif scenario == "ingest-retrieve" and self.command == "POST" and path == "/v1/memories:retrieve":
                assert current == "COMPLETED", "retrieval before indexing"
                assert body["message"] == "what does GoodMem do?"
                assert [key["spaceId"] for key in body["spaceKeys"]] == [SPACE]
                event = {"retrievedItem": {"chunk": {"resultSetId": SPACE, "memoryIndex": 0, "relevanceScore": 0.8,
                    "chunk": {"chunkId": SPACE, "memoryId": MEMORY, "chunkText": "indexed passage",
                              "chunkSequenceNumber": 0, "vectorStatus": "COMPLETED", **AUDIT}}}}
                self.reply(json.dumps(event) + "\n", "application/x-ndjson")
            elif scenario == "register-embedder" and self.command == "POST" and path == "/v1/embedders":
                assert body["displayName"] == "Document embeddings"
                assert body["modelIdentifier"] == "text-embedding-3-small"
                assert body["providerType"] == "OPENAI" and body["dimensionality"] == 1536
                assert body["endpointUrl"] == "https://api.openai.com/v1"
                assert body["distributionType"] == "DENSE"
                assert body["credentials"] == {"kind": "CREDENTIAL_KIND_API_KEY", "apiKey": {"inlineSecret": "sk_fixture_provider"}}
                self.reply({**{k: v for k, v in body.items() if k != "credentials"},
                            "embedderId": MEMORY, "ownerId": SPACE, "labels": {}, "supportedModalities": ["TEXT"], **AUDIT})
            elif scenario == "issue-scoped-key" and self.command == "POST" and path == "/v1/apikeys":
                assert body["authorityMode"] == "SCOPED"
                expected = [
                    {"operation": op, "selector": selector, "assignedResource": {"kind": "SPACE", "resourceId": SPACE}}
                    for op, selector in [("LIST_MEMORY", "EXACT"), ("READ_MEMORY", "DIRECT_MEMBERS_OF")]
                ]
                assert body["ceiling"] == expected
                assert not body.get("subjectPrincipalId"), "example must use current human principal"
                self.reply({"rawApiKey": "gm_fixture_new_secret", "apiKeyMetadata": {
                    "apiKeyId": MEMORY, "subjectPrincipalId": SPACE, "ownerPrincipalId": SPACE,
                    "authorityMode": "SCOPED", "ceiling": expected, "ceilingOmitted": False,
                    "keyPrefix": "gm_fixture", "status": "ACTIVE", "lifecycleState": "USABLE",
                    "labels": {}, "validFrom": 1, **AUDIT,
                }})
            else:
                raise AssertionError(f"Unexpected request: {self.command} {self.path}")

        def do_request(self):
            try:
                self.handle_request()
            except Exception as error:
                errors.append(repr(error))
                self.send_error(400, "fixture contract mismatch")

        do_GET = do_POST = do_request

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        result = subprocess.run(command, cwd=cwd, env={**os.environ,
            "GOODMEM_BASE_URL": f"http://127.0.0.1:{server.server_port}",
            "GOODMEM_API_KEY": "gm_fake_fixture", "GOODMEM_SPACE_ID": SPACE,
            "OPENAI_API_KEY": "sk_fixture_provider",
        }, text=True, capture_output=True, timeout=30)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    assert not errors, (errors, calls, result.stderr)
    if failed:
        assert result.returncode != 0 and "processing failed" in result.stderr, result
        assert polls == 1 and len(calls) == 2, calls
    else:
        assert result.returncode == 0, result.stderr
        if scenario == "ingest-retrieve":
            assert polls == 2 and "indexed passage" in result.stdout and len(calls) == 4, (calls, result.stdout)
        elif scenario == "list-spaces":
            assert SPACE in result.stdout and MEMORY in result.stdout and len(calls) == 2, (calls, result.stdout)
        else:
            assert MEMORY in result.stdout and len(calls) == 1, (calls, result.stdout)
    assert "sk_fixture_provider" not in result.stdout + result.stderr
    assert "gm_fixture_new_secret" not in result.stdout + result.stderr
    print(f"PASS {language}/{scenario}{' (processing failure)' if failed else ''}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("language", choices=["python", "typescript", "java", "dotnet"])
    parser.add_argument("--examples", required=True, type=Path)
    args = parser.parse_args()
    examples = args.examples.resolve()
    manifest = json.loads((examples / "examples.json").read_text())
    for scenario, command in manifest[args.language].items():
        command = [sys.executable if arg == "{python}" else arg for arg in command]
        run(args.language, scenario, command, examples)
        if scenario == "ingest-retrieve":
            run(args.language, scenario, command, examples, failed=True)
