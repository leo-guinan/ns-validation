import json
import unittest
from pathlib import Path


class FullTargetCompositionAuditTests(unittest.TestCase):
    def test_delta_composition_and_full_target_reoptimization(self):
        receipt = json.loads(Path("data/full-target-composition-audit.json").read_text())
        scope = receipt["frontier_scope"]
        audit = receipt["delta_interface_audit"]
        comp = receipt["composition_overhead"]
        full = receipt["full_target_optimization"]
        self.assertEqual(receipt["status"], "full_target_graph_audited")
        self.assertEqual(scope["target_size"], 2522)
        self.assertTrue(scope["nested"])
        self.assertTrue(scope["disjoint_delta_partition"])
        self.assertEqual(audit["I2436_union_I72"]["target_wide_coverage"], 2522)
        self.assertEqual(comp["I2436_union_I72_size"], 314)
        self.assertEqual(full["minimum_cover_width"], 309)
        self.assertEqual(full["uniqueness_status"], "falsified_at_least_two_distinct_optima")
        evidence = full["distinct_optima_evidence"]
        self.assertTrue(evidence["recorded_delta_I2508_is_full_target_optimum"])
        self.assertTrue(evidence["independent_full_target_witness_is_full_target_optimum"])
        self.assertEqual(evidence["intersection_size"], 308)
        self.assertTrue(evidence["sets_distinct"])


if __name__ == "__main__":
    unittest.main()
