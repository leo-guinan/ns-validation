import json
import unittest
from pathlib import Path


class MinimumChurn310CoverTests(unittest.TestCase):
    def test_exact_minimum_churn_is_localized(self):
        receipt = json.loads(Path("data/minimum-churn-310-cover.json").read_text())
        self.assertEqual(receipt["status"], "superseded_frontier_scope_error")
        self.assertTrue(receipt["scope_correction"]["full_frontier_claims_withdrawn"])
        self.assertTrue(receipt["scope_correction"]["raw_measurements_preserved"])


if __name__ == "__main__":
    unittest.main()
