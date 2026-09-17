import json
import unittest
from pathlib import Path


class OptimalFaceScopeRedundancyTests(unittest.TestCase):
    def test_all_inherited_noncoverage_cases_are_proven_infeasible(self):
        receipt = json.loads(Path("data/optimal-face-scope-redundancy.json").read_text())
        self.assertEqual(receipt["status"], "exact_inherited_noncoverage_sweep_complete")
        self.assertEqual(len(receipt["tests"]), 14)
        self.assertTrue(all(t["status"] == "proven_infeasible" for t in receipt["tests"]))
        self.assertEqual(receipt["summary"]["feasible_noncoverage_count"], 0)
        self.assertEqual(receipt["summary"]["proven_infeasible_count"], 14)
        self.assertEqual(receipt["summary"]["timeout_count"], 0)
        self.assertEqual(receipt["summary"]["optimal_family_relation"], "delta_optima_equal_full_optima")
        self.assertTrue(receipt["scope_relations"]["frontier_delta_subset_full"])
        self.assertIn("Feas(C_full)", receipt["scope_relations"]["feasible_cover_families"])


if __name__ == "__main__":
    unittest.main()
