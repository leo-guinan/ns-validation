import json
import unittest
from pathlib import Path


class FrontierAnatomyTests(unittest.TestCase):
    def test_graph_and_coverage_are_separate_from_trust_claims(self):
        receipt = json.loads(Path("data/frontier-anatomy.json").read_text())
        self.assertEqual(receipt["graph"]["local_declarations"], 892)
        self.assertEqual(receipt["graph"]["frontier_declarations"], 2450)
        self.assertEqual(receipt["graph"]["edges"], 85179)
        self.assertEqual(receipt["coverage"]["top_reuse"]["frontier_declarations"], 107)
        self.assertEqual(receipt["coverage"]["top_reuse_90"]["frontier_declarations"], 537)
        self.assertEqual(receipt["coverage"]["top_reuse_99"]["frontier_declarations"], 1681)
        self.assertEqual(receipt["grouping"]["defining_module"], "unavailable_from_ConstantInfo")


if __name__ == "__main__":
    unittest.main()
