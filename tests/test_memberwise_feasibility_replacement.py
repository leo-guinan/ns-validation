import json
import unittest
from pathlib import Path


class MemberwiseFeasibilityReplacementTests(unittest.TestCase):
    def test_memberwise_necessity_is_separate_from_optimality(self):
        receipt = json.loads(Path("data/memberwise-feasibility-replacement.json").read_text())
        self.assertEqual(receipt["experiment"], "27-memberwise-feasibility-replacement")
        self.assertEqual(receipt["summary"]["i72_infeasible_count"], 12)
        self.assertEqual(receipt["summary"]["a4_infeasible_count"], 0)
        self.assertEqual(receipt["summary"]["valid_309_witness_count"], 0)
        self.assertTrue(receipt["summary"]["all_i72_have_original_private_witness"])
        a4 = [r for r in receipt["members"] if r["group"] == "A4"]
        self.assertEqual([r["upper_bound"] for r in a4], [310, 311, 310, 311])
        self.assertEqual([r["lower_bound"] for r in a4], [310, 310, 310, 310])
        self.assertEqual([r["replacement_penalty_lower_bound"] for r in a4], [1, 1, 1, 1])
        self.assertTrue(all(r["witness"] for r in receipt["members"] if r["group"] == "A4"))


if __name__ == "__main__":
    unittest.main()
