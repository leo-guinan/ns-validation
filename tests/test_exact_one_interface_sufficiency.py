import json
import unittest
from pathlib import Path


class ExactOneInterfaceSufficiencyTests(unittest.TestCase):
    def test_reconstruction_and_disjoint_bounds(self):
        r = json.loads(Path("data/exact-one-interface-sufficiency.json").read_text())
        self.assertEqual(r["status"], "exact_one_interface_sufficiency_measured")
        self.assertEqual([(x["component_index"], x["optimum_count"], x["reconstructed_count"], x["false_positive_count"], x["maximum_pairwise_disjoint_exact_one_neighborhoods"], x["lower_bound_tight"]) for x in r["components"]], [(8, 48, 144, 96, 3, True), (11, 902, 10584, 9682, 3, True), (12, 1, 1, 0, 1, True), (21, 1, 1, 0, 2, True), (45, 1, 1, 0, 1, True)])
        self.assertTrue(all(x["opt_subset_reconstructed"] and x["OE_transpose_all_ones"] for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
