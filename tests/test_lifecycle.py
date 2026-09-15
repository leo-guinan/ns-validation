import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation import build_lifecycle_ledger, render_lifecycle_report


class LifecycleLedgerTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.ledger = build_lifecycle_ledger(root / "data/proof-stages.json", root / "data/source-ledger.json")

    def test_native_observations_are_preserved(self):
        search = self.ledger["stages"][0]
        values = {item["measure"]: item["value"] for item in search["work"]["observations"]}
        self.assertEqual(values["hours"], 88)
        self.assertEqual(values["messages"], 2700000)
        self.assertEqual(values["output_tokens"], 130000000000)

    def test_missing_costs_and_sizes_are_not_invented(self):
        for stage in self.ledger["stages"]:
            self.assertIsNone(stage["work"]["construction"]["value"])
            self.assertIsNone(stage["work"]["validation"]["value"])
            self.assertIsNone(stage["work"]["replay"]["value"])
            self.assertIsNone(stage["exported_state"]["size"]["value"])
            self.assertIsNone(stage["edgewise_compression_ratio"]["value"])

    def test_report_names_unsupported_metrics(self):
        report = render_lifecycle_report(self.ledger)
        self.assertIn("verification_compression_ratio", "\n".join(self.ledger["unsupported_metrics"]))
        self.assertIn("unknown", report)
        self.assertIn("Supported numeric metrics:", report)


if __name__ == "__main__":
    unittest.main()
