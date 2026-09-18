import json
import unittest
from pathlib import Path


class ExactWitnessNetworkRobustnessTests(unittest.TestCase):
    def test_component_robustness_and_single_failure_taxonomy(self):
        r = json.loads(Path("data/exact-witness-network-robustness.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_world_failure_robustness_measured")
        self.assertEqual(s["component_count"], 125)
        self.assertEqual(s["pure_substitution_count"], 120)
        self.assertTrue(s["pure_substitution_tau_kappa_equal"])
        self.assertEqual(s["tau_less_kappa_count"], 4)
        self.assertEqual(r["global_thresholds"]["tau_full"], 1)
        self.assertEqual(r["global_thresholds"]["kappa_full"], 1)
        self.assertEqual(len(r["single_failure_taxonomy"]["residual_backbone_worlds"]), 4)
        self.assertTrue(all(x["post_deletion_feasible"] for x in r["single_failure_taxonomy"]["residual_backbone_worlds"]))
        self.assertTrue(all(x["post_deletion_minimum_width"] > 1 for x in r["single_failure_taxonomy"]["residual_backbone_worlds"]))


if __name__ == "__main__":
    unittest.main()
