import json
import unittest
from pathlib import Path

from ns_validation.optimization_contract import contract_fingerprint


class HistoricalDeltaContractReplayTests(unittest.TestCase):
    def test_unavailable_replay_is_explicit(self):
        receipt = json.loads(Path("data/historical-delta-contract-replay.json").read_text())
        self.assertEqual(receipt["status"], "historical_contract_replay_unavailable_under_current_budget")
        self.assertEqual(receipt["replay_observation"]["nodes_emitted"], 2)
        self.assertEqual(receipt["replay_observation"]["nodes_requested"], 6)
        self.assertIsNone(receipt["contract_components"]["H_contract"])
        self.assertIsNone(receipt["replay_result"]["j_full_coverage"])

    def test_contract_fingerprint_is_deterministic(self):
        a = contract_fingerprint(["l2", "l1"], ["f1"], [["l1", "f1"]], {"objective": "min"}, {"width": 2})
        b = contract_fingerprint(["l2", "l1"], ["f1"], [["l1", "f1"]], {"objective": "min"}, {"width": 2})
        self.assertEqual(a, b)
        self.assertEqual(set(a), {"h_L", "h_F", "h_E", "h_O", "h_K", "H_contract"})


if __name__ == "__main__":
    unittest.main()
