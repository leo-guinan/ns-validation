import json
import unittest
from pathlib import Path


class SurgicalHistoricalContractReplayTests(unittest.TestCase):
    def test_nodes_reproduce_but_optimization_contract_does_not(self):
        receipt = json.loads(Path("data/surgical-historical-contract-replay.json").read_text())
        self.assertEqual(receipt["status"], "node_extraction_exactly_regenerated_optimization_contract_unavailable")
        self.assertEqual(receipt["node_reproduction"]["target"]["frontier_count"], 2522)
        self.assertEqual(receipt["delta_reconstruction"]["frontier_size"], 2508)
        self.assertTrue(receipt["isolation_falsifier"]["edge_equal_to_six_node_prefix"])
        self.assertEqual(receipt["optimization_contract"]["historical_candidate_count_reported"], 882)
        self.assertEqual(receipt["optimization_contract"]["regenerated_raw_target_minus_source_local_count"], 909)
        counts = receipt["candidate_count_provenance"]
        self.assertEqual(counts["later_reconstructed_inferred_delta_local_universe"], 741)
        self.assertTrue(counts["scopes_are_not_assumed_equal"])
        self.assertEqual(counts["reported_gap_909_to_882"], 27)
        self.assertEqual(counts["reported_gap_882_to_741"], 141)
        self.assertIsNone(receipt["optimization_contract"]["H_contract"])
        self.assertEqual(receipt["j_full_replay"]["status"], "not_performed")


if __name__ == "__main__":
    unittest.main()
