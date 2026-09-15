import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation import parse_markdown, render_report, write_json


class ProcessorTests(unittest.TestCase):
    def test_extracts_conservative_ledger_and_source_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "ideas.md"
            source.write_text(
                "Hard global construction can sometimes be replaced by iterative cancellation of a compressed local residual.\n"
                "OpenAI reports 10,000 agents and 130 billion output tokens.\n"
                "How much information crosses each proof boundary?\n"
                "This does not establish the hypothesis.\n",
                encoding="utf-8",
            )
            ledger = parse_markdown(source)
            self.assertEqual(ledger.source_sha256, hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(len(ledger.claims), 1)
            self.assertGreaterEqual(len(ledger.metrics), 2)
            self.assertEqual(len(ledger.research_questions), 1)
            self.assertEqual(len(ledger.boundaries), 1)
            self.assertEqual(ledger.claims[0].status, "unvalidated")

    def test_json_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "ideas.md"
            output = Path(tmp) / "ledger.json"
            source.write_text("More expensive discovery can justify cheaper future truth.\n", encoding="utf-8")
            ledger = parse_markdown(source)
            write_json(ledger, output)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["source_sha256"], ledger.source_sha256)
            self.assertEqual(payload["claims"][0]["status"], "unvalidated")

    def test_report_is_readable(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "ideas.md"
            source.write_text("Different stages of truth production want different computers.\n", encoding="utf-8")
            report = render_report(parse_markdown(source))
            self.assertIn("Validation ideas report", report)
            self.assertIn("Claims (unvalidated): 1", report)


if __name__ == "__main__":
    unittest.main()
