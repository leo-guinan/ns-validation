import json
import unittest
from pathlib import Path


class SubinterfaceEmbeddingCounterfactualTests(unittest.TestCase):
    def test_literal_embedding_and_counterfactual_boundary(self):
        receipt = json.loads(Path("data/subinterface-embedding-counterfactuals.json").read_text())
        self.assertEqual(receipt["status"], "superseded_frontier_scope_error")
        self.assertTrue(receipt["scope_correction"]["full_frontier_claims_withdrawn"])
        self.assertTrue(receipt["scope_correction"]["raw_measurements_preserved"])


if __name__ == "__main__":
    unittest.main()
