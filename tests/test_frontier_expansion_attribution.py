import json
import unittest
from pathlib import Path


class FrontierExpansionAttributionTests(unittest.TestCase):
    def test_all_frontier_expansions_are_attributed_at_entry(self):
        receipt = json.loads(Path("data/frontier-expansion-attribution.json").read_text())
        self.assertEqual(receipt["experiment"], "17-frontier-expansion-attribution")
        self.assertEqual(receipt["summary"]["expanding_edges"], 6)
        self.assertEqual(receipt["summary"]["active_at_entry_fraction"], [1.0] * 6)
        self.assertIn("does not establish runtime causality", receipt["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
