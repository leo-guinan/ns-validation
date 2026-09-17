import json
import unittest
from pathlib import Path


class SubinterfaceEmbeddingCounterfactualTests(unittest.TestCase):
    def test_literal_embedding_and_counterfactual_boundary(self):
        receipt = json.loads(Path("data/subinterface-embedding-counterfactuals.json").read_text())
        self.assertEqual(receipt["experiment"], "26-subinterface-embedding-counterfactuals")
        self.assertTrue(receipt["embedding"]["frontier_sets_equal"])
        self.assertTrue(receipt["embedding"]["edge_sets_equal"])
        self.assertEqual(receipt["embedding"]["standalone_degree_vector"], receipt["embedding"]["inserted_degree_vector"])
        self.assertEqual(receipt["counterfactuals"]["forbid_i72"]["status"], "infeasible")
        self.assertEqual(receipt["counterfactuals"]["forbid_other_additions"]["status"], "exact_from_unique_baseline_and_witness")
        self.assertEqual(receipt["counterfactuals"]["forbid_other_additions"]["optimum"], 310)
        self.assertEqual(len(receipt["counterfactuals"]["forbid_other_additions"]["witness"]), 310)


if __name__ == "__main__":
    unittest.main()
