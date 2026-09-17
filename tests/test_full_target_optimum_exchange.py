import json
import unittest
from pathlib import Path


class FullTargetOptimumExchangeTests(unittest.TestCase):
    def test_exchange_and_composition_are_separate(self):
        receipt = json.loads(Path("data/full-target-optimum-exchange.json").read_text())
        self.assertEqual(receipt["status"], "exact_width_309_forbidden_member_sweep_complete")
        optimum = receipt["independent_optimum"]
        self.assertEqual(optimum["size"], 309)
        self.assertEqual(optimum["intersection_with_I2508"], 308)
        self.assertEqual(optimum["symmetric_difference"], 2)
        self.assertEqual(receipt["member_sweep"]["tested_count"], 309)
        self.assertEqual(receipt["member_sweep"]["feasible_count"], 59)
        comp = receipt["composition_anatomy"]
        self.assertEqual(comp["size"], 314)
        self.assertEqual(comp["net_overhead"], 5)
        self.assertEqual(comp["symmetric_difference_size"], 15)
        self.assertFalse(comp["pure_deletion"])
        contract = receipt["contract"]["old_delta_contract_audit"]
        self.assertEqual(contract["status"], "edge_relation_not_replayable_from_preserved_artifacts")
        self.assertTrue(contract["tensorDiff_divergence_in_inferred_delta_local_universe"])
        self.assertTrue(contract["weak_pressure_poisson_in_inferred_delta_local_universe"])
        self.assertEqual(contract["candidate_vocabulary_difference_explains_exchange"], "not_explained_by_reconstructed_vocabulary")
        self.assertFalse(contract["old_delta_edge_lists_preserved"])


if __name__ == "__main__":
    unittest.main()
