"""Ensure context checks fail when an entry or detail page grows too large."""
import shutil
import tempfile
import unittest
from pathlib import Path

import context


class ContextBudgets(unittest.TestCase):
    def test_all_twelve_workflow_routes_fit(self):
        report = context.measure()
        self.assertEqual(len(report["routes"]), 12)
        for route in report["routes"]:
            self.assertLessEqual(route["tokens"], context.TASK_LIMIT)
            self.assertEqual(route["files"][0]["file"], "SKILL.md")
            self.assertEqual(route["tokens"], sum(p["tokens"] for p in route["files"]))

    def test_oversized_entries_and_details_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(context.SKILL.parent, root, dirs_exist_ok=True)
            for relative in ["SKILL.md", "references/java.md", "references/java/memories.md",
                             "references/java/memories/create.md", "references/java/models/CreateApiKeyRequest.md"]:
                with self.subTest(file=relative):
                    path = root / relative
                    original = path.read_text()
                    path.write_text(original + "\n" + "growth " * 2100)
                    with self.assertRaisesRegex(ValueError, "tokens exceeds"):
                        context.measure(root / "SKILL.md")
                    path.write_text(original)


if __name__ == "__main__":
    unittest.main()
