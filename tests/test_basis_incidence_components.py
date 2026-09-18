import json
import unittest
from pathlib import Path


class BasisIncidenceComponentsTests(unittest.TestCase):
    def test_component_factorization_and_exact_backbone(self):
        receipt = json.loads(Path("data/basis-incidence-components.json").read_text())
        self.assertEqual(receipt["status"], "exact_component_minima_and_optimum_families_measured")
        self.assertEqual(receipt["summary"]["component_count"], 302)
        self.assertEqual(receipt["summary"]["basis_class_count"], 320)
        self.assertEqual(receipt["summary"]["minimum_width_sum"], 309)
        self.assertEqual(receipt["summary"]["slack_sum"], 11)
        self.assertEqual(receipt["summary"]["global_backbone_count"], 250)
        self.assertEqual(receipt["exchange_location"]["component"], 31)
        self.assertTrue(all(c["enumeration_status"] == "complete" for c in receipt["components"]))


if __name__ == "__main__":
    unittest.main()
