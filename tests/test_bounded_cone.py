import json
import unittest
from pathlib import Path


class BoundedConeTests(unittest.TestCase):
    def test_boundary_counts_and_unknown_full_cone(self):
        receipt = json.loads(Path("data/bounded-cone.json").read_text())
        self.assertEqual(receipt["counts"]["direct"], 2)
        self.assertEqual(receipt["counts"]["local_cone"], 892)
        self.assertEqual(receipt["counts"]["frontier"], 2450)
        self.assertEqual(receipt["counts"]["max_local_depth"], 25)
        self.assertEqual(len(receipt["local_cone"]), 892)
        self.assertEqual(len(receipt["external_frontier"]), 2450)
        self.assertIsNone(receipt["full_unbounded_cone"])
        self.assertIsNone(receipt["activation_ratio"])


if __name__ == "__main__":
    unittest.main()
