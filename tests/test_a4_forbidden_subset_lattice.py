import json
import unittest
from pathlib import Path


class A4ForbiddenSubsetLatticeTests(unittest.TestCase):
    def test_all_subsets_are_feasible_and_nonempty_cost_one(self):
        receipt = json.loads(Path("data/a4-forbidden-subset-lattice.json").read_text())
        self.assertEqual(receipt["experiment"], "28-a4-forbidden-subset-lattice")
        self.assertEqual(receipt["summary"]["subset_count"], 16)
        self.assertEqual(receipt["summary"]["feasible_count"], 16)
        self.assertEqual(receipt["summary"]["infeasible_count"], 0)
        self.assertEqual(receipt["summary"]["minimal_infeasible_count"], 0)
        self.assertEqual(receipt["summary"]["exact_count"], 15)
        self.assertEqual(receipt["penalty_function"], {"empty": 0, "nonempty": 1})
        self.assertTrue(receipt["universal_nonempty_witness"]["valid"])
        for row in receipt["subsets"]:
            if row["forbidden_subset"]:
                self.assertEqual(row["optimum"], 310)
                self.assertEqual(row["replacement_penalty"], 1)


if __name__ == "__main__":
    unittest.main()
