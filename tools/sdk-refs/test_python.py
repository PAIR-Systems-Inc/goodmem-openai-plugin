"""Execute the documented quick start through the published SDK and an HTTP fixture."""
import ast
import contextlib
import importlib.util
import inspect
import io
import json
import os
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import goodmem
import httpx
from goodmem import Goodmem

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SKILL = ROOT / "plugins/goodmem/skills/goodmem-sdk/SKILL.md"
REFS = SKILL.parent / "references"
MATRIX = json.loads((HERE / "versions.json").read_text())
SPACE = "00000000-0000-0000-0000-000000000001"
MEMORY = "00000000-0000-0000-0000-000000000002"


class Examples(unittest.TestCase):
    def run_example(self, states, tick=0.5):
        calls = []
        time = 0
        current = "PENDING"

        def now():
            nonlocal time
            time += tick
            return time

        def handler(request):
            nonlocal current
            calls.append((request.method, request.url.path))
            if request.method == "POST" and request.url.path == "/v1/memories:retrieve":
                self.assertEqual(current, "COMPLETED", "retrieved before indexing completed")
                event = {"retrievedItem": {"chunk": {
                    "resultSetId": SPACE, "memoryIndex": 0, "relevanceScore": 0.8,
                    "chunk": {"chunkText": "indexed passage", "chunkId": SPACE,
                        "memoryId": MEMORY, "chunkSequenceNumber": 0, "vectorStatus": "COMPLETED",
                        "createdAt": 1, "updatedAt": 1, "createdById": SPACE, "updatedById": SPACE},
                }}}
                return httpx.Response(200, text=json.dumps(event) + "\n", headers={"content-type": "application/x-ndjson"})
            if request.method == "GET":
                current = next(states, current)
            return httpx.Response(200, json={
                "memoryId": MEMORY, "spaceId": SPACE, "originalContentRef": "",
                "contentType": "text/plain", "processingStatus": current,
                "pageImageStatus": "UNSPECIFIED", "pageImageCount": 0,
                "createdAt": 1, "updatedAt": 1, "createdById": SPACE, "updatedById": SPACE,
                "metadata": {},
            })

        def client(**_):
            return Goodmem(http_client=httpx.Client(base_url="https://example.invalid", transport=httpx.MockTransport(handler)))

        example = REFS / "python/examples/ingest-retrieve.md"
        snippet = re.search(r"```python\n(.*?)\n```", example.read_text(), re.S)[1]
        output = io.StringIO()
        with patch("goodmem.Goodmem", client), patch("time.sleep"), patch("time.monotonic", now), patch.dict(os.environ, {
            "GOODMEM_BASE_URL": "https://example.invalid", "GOODMEM_API_KEY": "gm_fake", "GOODMEM_SPACE_ID": SPACE,
        }), contextlib.redirect_stdout(output):
            exec(compile(snippet, str(example), "exec"), {})
        return calls, output.getvalue()

    def test_waits_for_indexing(self):
        calls, output = self.run_example(iter(["PROCESSING", "COMPLETED"]))
        self.assertEqual(sum(method == "GET" for method, _ in calls), 2)
        self.assertEqual(output.strip(), "indexed passage")

    def test_failed_ingestion_stops(self):
        with self.assertRaisesRegex(RuntimeError, "processing failed"):
            self.run_example(iter(["FAILED"]))

    def test_pending_ingestion_has_a_deadline(self):
        with self.assertRaisesRegex(TimeoutError, "still processing"):
            self.run_example(iter([]), tick=61)

    def test_documented_python_parameters_exist_in_the_published_package(self):
        self.assertEqual(goodmem.__version__, MATRIX["packages"]["python"]["version"])
        methods = []
        for path in (REFS / "python").glob("*/*.md"):
            if path.parent.name not in {"models", "examples"}:
                methods.extend(re.findall(r"^([\w.]+)\((.*?)\)(?: -> .*?)?$", path.read_text(), re.M))
        self.assertGreater(len(methods), 40)
        with Goodmem(base_url="https://example.invalid", api_key="gm_fake") as client:
            for name, params in methods:
                with self.subTest(method=name):
                    target = client
                    for part in name.split("."):
                        target = getattr(target, part)
                    signature = inspect.signature(target)
                    args = ast.parse(f"def example({params}): pass").body[0].args
                    documented = {arg.arg for arg in args.args + args.kwonlyargs}
                    self.assertLessEqual(documented, set(signature.parameters))


class Freshness(unittest.TestCase):
    def test_missing_or_mismatched_stamp_is_an_error(self):
        spec = importlib.util.spec_from_file_location("freshness", HERE / "freshness.py")
        freshness = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(freshness)
        with tempfile.TemporaryDirectory() as directory:
            refs = Path(directory)
            shutil.copytree(REFS, refs, dirs_exist_ok=True)
            freshness.validate(refs, MATRIX)
            detail = refs / "python/memories/create.md"
            detail.write_text(detail.read_text().replace("version=0.1.34", "version=0.0.0"))
            with self.assertRaises(ValueError):
                freshness.validate(refs, MATRIX)
            detail.write_text((REFS / "python/memories/create.md").read_text())
            (refs / "python.md").write_text("# unstamped\n")
            with self.assertRaises(ValueError):
                freshness.validate(refs, MATRIX)
            (refs / "python.md").unlink()
            with self.assertRaises(ValueError):
                freshness.validate(refs, MATRIX)


if __name__ == "__main__":
    unittest.main()
