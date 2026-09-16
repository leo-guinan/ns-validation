import json
import unittest
from pathlib import Path


class TransitionAnatomyTests(unittest.TestCase):
    def test_distribution_preserves_both_transition_types(self):
        receipt = json.loads(Path("data/transition-anatomy.json").read_text())
        self.assertEqual(receipt["distribution"]["transition_count"], 12)
        self.assertEqual(receipt["distribution"]["class_counts"], {"frontier_unchanged": 6, "frontier_expanding": 6})
        self.assertIn(0, receipt["distribution"]["delta_frontier"])
        self.assertIn(2508, receipt["distribution"]["delta_frontier"])
        self.assertEqual(receipt["falsifier"]["result"], "small_and_expanding_transitions_both_observed")


if __name__ == "__main__":
    unittest.main()
