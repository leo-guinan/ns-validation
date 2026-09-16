import json
import unittest
from pathlib import Path


class InterfaceEditAnatomyTests(unittest.TestCase):
    def test_edit_arithmetic_and_small_interface_insertion(self):
        receipt = json.loads(Path("data/interface-edit-anatomy.json").read_text())
        comparison = receipt["comparison"]
        small = receipt["small_interface_test"]
        self.assertEqual(receipt["experiment"], "24-interface-edit-anatomy")
        self.assertEqual((comparison["removed_count"], comparison["added_count"], comparison["symmetric_difference_count"], comparison["net_width_change"]), (9, 16, 25, 7))
        self.assertTrue(small["small_subset_added"])
        self.assertEqual(small["small_added_intersection_count"], 12)
        self.assertEqual(small["small_shared_intersection_count"], 0)
        self.assertEqual(comparison["overlap_edge_count"], 138)


if __name__ == "__main__":
    unittest.main()
