#!/usr/bin/env python3
"""Run an extracted SDK example against a local HTTP fixture, never a real instance."""
import argparse
import json
import os
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

SPACE = "00000000-0000-0000-0000-000000000001"
MEMORY = "00000000-0000-0000-0000-000000000002"


def run(language, command, failed=False):
    calls = []
    polls = 0
    current = "PENDING"

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

        def do_GET(self):
            nonlocal polls, current
            calls.append(("GET", self.path))
            if self.path.startswith("/v1/spaces"):
                query = parse_qs(urlsplit(self.path).query)
                final = "nextToken" in query
                self.reply({"spaces": [{
                    "spaceId": MEMORY if final else SPACE, "name": "second-page" if final else "first-page", "ownerId": SPACE,
                    "spaceEmbedders": [], "labels": {}, "createdAt": 1, "updatedAt": 1,
                    "createdById": SPACE, "updatedById": SPACE,
                }], **({} if final else {"nextToken": "next"})})
                return
            if self.path.startswith(f"/v1/memories/{MEMORY}"):
                polls += 1
                current = "FAILED" if failed else ("COMPLETED" if polls >= 2 else "PROCESSING")
                self.reply(self.memory())
                return
            self.send_error(404)

        def memory(self):
            return {"memoryId": MEMORY, "spaceId": SPACE, "originalContentRef": "",
                "contentType": "text/plain", "processingStatus": current, "pageImageStatus": "UNSPECIFIED",
                "pageImageCount": 0, "createdAt": 1, "updatedAt": 1, "createdById": SPACE,
                "updatedById": SPACE, "metadata": {}}

        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length", 0)))
            calls.append(("POST", self.path))
            if self.path == "/v1/memories":
                self.reply(self.memory())
            elif self.path == "/v1/memories:retrieve":
                if current != "COMPLETED":
                    self.send_error(409, "retrieval before indexing")
                    return
                event = {"retrievedItem": {"chunk": {"resultSetId": SPACE, "memoryIndex": 0, "relevanceScore": 0.8,
                    "chunk": {"chunkId": SPACE, "memoryId": MEMORY, "chunkText": "indexed passage",
                        "chunkSequenceNumber": 0, "vectorStatus": "COMPLETED", "createdAt": 1,
                        "updatedAt": 1, "createdById": SPACE, "updatedById": SPACE}}}}
                self.reply(json.dumps(event) + "\n", "application/x-ndjson")
            else:
                self.send_error(404)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        result = subprocess.run(command, env={**os.environ,
            "GOODMEM_BASE_URL": f"http://127.0.0.1:{server.server_port}",
            "GOODMEM_API_KEY": "gm_fake_fixture", "GOODMEM_SPACE_ID": SPACE,
        }, text=True, capture_output=True, timeout=30)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    if failed:
        assert result.returncode != 0 and "processing failed" in result.stderr, result
        assert not any(path == "/v1/memories:retrieve" for _, path in calls), calls
    else:
        assert result.returncode == 0, result.stderr
        if language == "java":
            assert polls == 2 and "indexed passage" in result.stdout, (calls, result.stdout)
        else:
            assert SPACE in result.stdout and MEMORY in result.stdout, (calls, result.stdout)
            assert len(calls) == 2, calls
    print(f"PASS {language}: {'processing failure stops retrieval' if failed else 'documented example executes through published SDK'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("language", choices=["typescript", "java", "dotnet"])
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    run(args.language, args.command)
    if args.language == "java":
        run(args.language, args.command, failed=True)
