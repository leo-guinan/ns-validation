import json
import unittest
from pathlib import Path


class ScopeActivationDepthTests(unittest.TestCase):
    def test_all_inherited_identities_are_globally_implied(self):
        receipt = json.loads(Path("data/scope-activation-depth.json").read_text())
        self.assertEqual(receipt["status"], "exact_scope_activation_sweep_complete")
        self.assertEqual(len(receipt["tests"]), 14)
        self.assertTrue(all(t["status"] == "infeasible" for t in receipt["tests"]))
        self.assertEqual(receipt["summary"]["optimal_count"], 0)
        self.assertEqual(receipt["summary"]["infeasible_count"], 14)
        self.assertEqual(receipt["summary"]["timeout_or_other_count"], 0)
        self.assertIsNone(receipt["summary"]["scope_activation_gap"])


if __name__ == "__main__":
    unittest.main()
