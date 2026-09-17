import json
import unittest
from pathlib import Path


class MemberwiseFeasibilityReplacementTests(unittest.TestCase):
    def test_memberwise_necessity_is_separate_from_optimality(self):
        receipt = json.loads(Path("data/memberwise-feasibility-replacement.json").read_text())
        self.assertEqual(receipt["status"], "superseded_frontier_scope_error")
        self.assertTrue(receipt["scope_correction"]["full_frontier_claims_withdrawn"])
        self.assertTrue(receipt["scope_correction"]["raw_measurements_preserved"])


if __name__ == "__main__":
    unittest.main()
