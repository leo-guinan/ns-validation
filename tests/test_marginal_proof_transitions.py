import json
import unittest
from pathlib import Path


class MarginalProofTransitionTests(unittest.TestCase):
    def test_reachable_transition_delta_is_recorded_without_generalizing(self):
        receipt = json.loads(Path("data/marginal-proof-transitions.json").read_text())
        self.assertEqual(len(receipt["nodes"]), 6)
        self.assertEqual(len(receipt["transitions"]), 12)
        pair = next(t for t in receipt["transitions"] if t["ancestor"].endswith("theorem_1_1_with_initial_rest") and t["descendant"].endswith("theorem_1_1"))
        self.assertEqual(pair["support"]["local_delta"], 2)
        self.assertEqual(pair["support"]["frontier_delta"], 0)
        self.assertIn("complete project theorem DAG", receipt["not_yet_measured"])


if __name__ == "__main__":
    unittest.main()
