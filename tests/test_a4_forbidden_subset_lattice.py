import json
import unittest
from pathlib import Path


class A4ForbiddenSubsetLatticeTests(unittest.TestCase):
    def test_all_subsets_are_feasible_and_nonempty_cost_one(self):
        receipt = json.loads(Path("data/a4-forbidden-subset-lattice.json").read_text())
        self.assertEqual(receipt["status"], "superseded_frontier_scope_error")
        self.assertTrue(receipt["scope_correction"]["full_frontier_claims_withdrawn"])
        self.assertTrue(receipt["scope_correction"]["raw_measurements_preserved"])


if __name__ == "__main__":
    unittest.main()
