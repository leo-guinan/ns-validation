import json
import unittest
from pathlib import Path


class MinimumChurn310CoverTests(unittest.TestCase):
    def test_exact_minimum_churn_is_localized(self):
        receipt = json.loads(Path("data/minimum-churn-310-cover.json").read_text())
        self.assertEqual(receipt["experiment"], "30-minimum-churn-310-cover")
        self.assertEqual(receipt["solver"]["status"], "optimal")
        self.assertTrue(receipt["alternative_witness"]["covers_frontier"])
        self.assertTrue(receipt["alternative_witness"]["excludes_a4"])
        self.assertTrue(receipt["alternative_witness"]["preserves_i72"])
        self.assertEqual(receipt["comparison"]["symmetric_difference_count"], 9)
        self.assertEqual(receipt["comparison"]["removed_count"], 4)
        self.assertEqual(receipt["comparison"]["added_count"], 5)
        self.assertEqual(receipt["comparison"]["collateral_removals_count"], 0)


if __name__ == "__main__":
    unittest.main()
