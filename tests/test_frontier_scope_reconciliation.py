import json
import unittest
from pathlib import Path


class FrontierScopeReconciliationTests(unittest.TestCase):
    def test_transition_deltas_reconcile_to_common_target(self):
        receipt = json.loads(Path("data/frontier-scope-reconciliation.json").read_text())
        checks = receipt["delta_identity_checks"]
        self.assertEqual(receipt["status"], "literal_frontier_scope_reconciled")
        self.assertEqual(len(receipt["frontiers"]["target"]), 2522)
        self.assertEqual(checks["delta_72_size"], 72)
        self.assertEqual(checks["delta_2508_size"], 2508)
        self.assertTrue(checks["delta_72_subset_delta_2508"])
        self.assertEqual(checks["delta_2508_only_size"], 2436)
        self.assertTrue(receipt["transition_comparisons"]["source_A_to_target"]["monotone"])
        self.assertTrue(receipt["transition_comparisons"]["source_B_to_target"]["monotone"])


if __name__ == "__main__":
    unittest.main()
