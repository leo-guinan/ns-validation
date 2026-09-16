import json
import unittest
from pathlib import Path


class EntryInterfaceAnatomyTests(unittest.TestCase):
    def test_access_width_is_separate_from_frontier_size(self):
        receipt = json.loads(Path("data/entry-interface-anatomy.json").read_text())
        self.assertEqual(receipt["experiment"], "18-entry-interface-anatomy")
        self.assertEqual(len(receipt["graphs"]), 6)
        self.assertEqual(receipt["summary"]["frontier_size"], [72, 72, 2436, 2436, 2436, 2508])
        self.assertEqual(receipt["summary"]["all_frontier_degree_positive"], True)
        self.assertIn("not an exact set-cover minimum", receipt["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
