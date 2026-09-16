import json
import unittest
from pathlib import Path


class VerificationCapitalReuseTests(unittest.TestCase):
    def test_reuse_and_domination_are_bounded(self):
        receipt = json.loads(Path("data/verification-capital-reuse.json").read_text())
        self.assertEqual(receipt["experiment"], "15-verification-capital-reuse")
        self.assertEqual(len(receipt["frontier_expansion_profiles"]), 6)
        self.assertEqual(sum(bool(x["dominates_selected_nodes"]) for x in receipt["domination"]["edge_dominators"]), 0)
        self.assertIn("selected six-node graph", receipt["interpretation_boundary"])
        self.assertIn("runtime cost causality", receipt["not_yet_measured"])


if __name__ == "__main__":
    unittest.main()
