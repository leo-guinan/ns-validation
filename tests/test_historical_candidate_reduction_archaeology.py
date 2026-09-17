import json
import unittest
from pathlib import Path


class HistoricalCandidateReductionArchaeologyTests(unittest.TestCase):
    def test_counts_and_missing_reduction_are_explicit(self):
        receipt = json.loads(Path("data/historical-candidate-reduction-archaeology.json").read_text())
        self.assertEqual(receipt["status"], "historical_candidate_reduction_partially_unrecovered")
        self.assertEqual(receipt["raw_input"]["count"], 909)
        self.assertEqual(receipt["reported_provenance_objects"]["L_882_reported"]["count"], 882)
        self.assertEqual(receipt["reported_provenance_objects"]["L_741_inferred"]["count"], 741)
        self.assertFalse(receipt["archaeology_search"]["exact_909_to_882_rule_found"])
        self.assertFalse(receipt["archaeology_search"]["preserved_exact_882_identity_list"])
        self.assertIsNone(receipt["reduction_outputs"]["R27"])
        self.assertIsNone(receipt["exchanged_declarations"]["in_L882_reported"])


if __name__ == "__main__":
    unittest.main()
