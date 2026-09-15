import json
import unittest
from pathlib import Path


class BoundarySweepTests(unittest.TestCase):
    def test_declared_boundaries_are_complete_and_unbounded_is_unknown(self):
        receipt = json.loads(Path("data/boundary-sweep.json").read_text())
        self.assertEqual(receipt["status"], "complete_for_declared_boundaries")
        self.assertEqual([b["local_declarations"] for b in receipt["boundaries"]], [1, 3, 892])
        self.assertEqual([b["frontier_declarations"] for b in receipt["boundaries"]], [2, 21, 2450])
        self.assertIsNone(receipt["full_unbounded_cone"])
        self.assertIsNone(receipt["minimal_boundary"])
        self.assertIsNone(receipt["optimization"])


if __name__ == "__main__":
    unittest.main()
