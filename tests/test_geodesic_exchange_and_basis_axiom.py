import json
import unittest
from pathlib import Path


class GeodesicExchangeAndBasisAxiomTests(unittest.TestCase):
    def test_geodesic_result_and_matroid_counterexample(self):
        r = json.loads(Path("data/geodesic-exchange-and-basis-axiom.json").read_text())
        self.assertEqual(r["status"], "exact_geodesic_and_basis_exchange_measured")
        self.assertTrue(r["summary"]["all_components_geodesic"])
        self.assertEqual(r["summary"]["maximum_detour"], 0)
        self.assertEqual(r["summary"]["global_diameter"], 59)
        self.assertFalse(r["summary"]["all_components_satisfy_basis_exchange_axiom"])
        self.assertEqual(r["summary"]["matroid_counterexample"]["component"], 9)
        self.assertEqual(r["diameter_witness"]["endpoint_size"], 309)
        self.assertEqual(r["diameter_witness"]["endpoint_intersection_size"], 250)
        self.assertEqual(r["diameter_witness"]["symmetric_difference_cardinality"], 118)
        self.assertEqual(r["diameter_witness"]["replacement_distance"], 59)
        self.assertEqual(r["diameter_witness"]["johnson_distance"], 59)
        self.assertEqual(r["diameter_witness"]["path_length"], 59)


if __name__ == "__main__":
    unittest.main()
