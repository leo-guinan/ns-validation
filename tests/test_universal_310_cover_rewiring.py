import json
import unittest
from pathlib import Path


class Universal310CoverRewiringTests(unittest.TestCase):
    def test_valid_witness_and_broad_rewrite(self):
        receipt = json.loads(Path("data/universal-310-cover-rewiring.json").read_text())
        self.assertEqual(receipt["experiment"], "29-universal-310-cover-rewiring")
        witness = receipt["alternative_witness"]
        comparison = receipt["comparison"]
        self.assertTrue(witness["covers_frontier"])
        self.assertTrue(witness["excludes_a4"])
        self.assertTrue(comparison["a4_subset_removed"])
        self.assertTrue(comparison["i72_subset_alternative"])
        self.assertEqual(comparison["added_count"], comparison["removed_count"] + 1)
        self.assertEqual(receipt["width_310_enumeration"]["status"], "not_attempted")


if __name__ == "__main__":
    unittest.main()
