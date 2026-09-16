import json
import unittest
from pathlib import Path


class ResponsibilityFlowAnatomyTests(unittest.TestCase):
    def test_frontier_flow_and_inserted_interface(self):
        receipt = json.loads(Path("data/responsibility-flow-anatomy.json").read_text())
        self.assertEqual(receipt["experiment"], "25-responsibility-flow-anatomy")
        self.assertEqual(receipt["frontier_sets"]["shared_count"], 2436)
        self.assertEqual(receipt["frontier_sets"]["lost_count"], 0)
        self.assertEqual(receipt["frontier_sets"]["new_count"], 72)
        self.assertTrue(receipt["summary"]["i72_subset_added"])
        self.assertEqual(receipt["summary"]["i72_added_count"], 12)
        self.assertEqual(receipt["summary"]["other_added_count"], 4)
        self.assertEqual(receipt["edit"]["nonzero_weight_edge_count"], 138)
        self.assertEqual(receipt["summary"]["flow_unaccounted_count"], 0)


if __name__ == "__main__":
    unittest.main()
