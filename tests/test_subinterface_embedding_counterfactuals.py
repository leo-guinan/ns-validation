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
        self.assertEqual(receipt["counterfactuals"]["forbid_other_additions"]["status"], "infeasible_by_unavailable_frontier_identity")
        self.assertEqual(receipt["counterfactuals"]["forbid_other_additions"]["unavailable_frontier_count"], 69)
        self.assertEqual(receipt["counterfactuals"]["forbid_other_additions"]["inherited_baseline_bound"], 309)


if __name__ == "__main__":
    unittest.main()
