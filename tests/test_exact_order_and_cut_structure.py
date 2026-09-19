import json
import unittest
from pathlib import Path


class ExactOrderAndCutStructureTests(unittest.TestCase):
    def test_ties_and_cut_relations(self):
        r = json.loads(Path("data/exact-order-and-cut-structure.json").read_text())
        self.assertEqual(r["status"], "exact_weak_order_and_exact_one_cut_structure_measured")
        self.assertEqual([(x["component_index"], x["equal_p_imply_equal_qtau"]) for x in r["components"]], [(8, False), (11, True), (12, True), (21, True), (45, True)])
        self.assertEqual([(x["component_index"], x["exact_one_neighborhood_pair_relations"]) for x in r["components"]], [(8, {"identical": 0, "disjoint": 0, "overlapping": 0}), (11, {"identical": 0, "disjoint": 1, "overlapping": 0}), (12, {"identical": 0, "disjoint": 0, "overlapping": 1}), (21, {"identical": 0, "disjoint": 1, "overlapping": 0}), (45, {"identical": 0, "disjoint": 0, "overlapping": 1})])


if __name__ == "__main__":
    unittest.main()
