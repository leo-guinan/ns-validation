import json
import unittest
from pathlib import Path


class Universal310CoverRewiringTests(unittest.TestCase):
    def test_valid_witness_and_broad_rewrite(self):
        receipt = json.loads(Path("data/universal-310-cover-rewiring.json").read_text())
        self.assertEqual(receipt["status"], "superseded_frontier_scope_error")
        self.assertTrue(receipt["scope_correction"]["full_frontier_claims_withdrawn"])
        self.assertTrue(receipt["scope_correction"]["raw_measurements_preserved"])


if __name__ == "__main__":
    unittest.main()
