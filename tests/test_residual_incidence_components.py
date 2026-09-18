import json
import unittest
from pathlib import Path


class ResidualIncidenceComponentsTests(unittest.TestCase):
    def test_component_factorization(self):
        r = json.loads(Path("data/residual-incidence-components.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_residual_incidence_components_measured")
        self.assertEqual(s["removal_component_count"], 125)
        self.assertEqual(s["addition_component_count"], 125)
        self.assertEqual(s["removal_coordinate_sum"], 142)
        self.assertEqual(s["removal_width_sum"], 130)
        self.assertTrue(s["removal_all_enumerated"])
        self.assertTrue(s["addition_all_enumerated"])
        self.assertEqual(sorted((x["coordinate_count"], x["candidate_world_count"], x["minimum_cover_width"]) for x in r["removal"]), sorted((x["coordinate_count"], x["candidate_world_count"], x["minimum_cover_width"]) for x in r["addition"]))


if __name__ == "__main__":
    unittest.main()
