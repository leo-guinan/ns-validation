import json
import unittest
from pathlib import Path


class ProofStageOverlapTests(unittest.TestCase):
    def test_only_source_supported_anchors_are_grounded(self):
        receipt = json.loads(Path("data/proof-stage-overlap.json").read_text())
        self.assertEqual(receipt["status"], "partial_support_only_source_supported_anchors")
        self.assertEqual(len(receipt["grounded_support"]), 2)
        self.assertEqual(receipt["pairwise_overlap"]["layers"]["module"]["jaccard"], 1.0)
        self.assertEqual(receipt["pairwise_overlap"]["layers"]["artifact"]["jaccard"], 1.0)
        self.assertEqual(receipt["falsifier"]["result"], "triggered")
        self.assertEqual(len(receipt["not_yet_measured"]), 5)


if __name__ == "__main__":
    unittest.main()
