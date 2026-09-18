import json
import unittest
from fractions import Fraction
from pathlib import Path


class ExactWitnessParticipationTests(unittest.TestCase):
    def test_participation_conservation_and_categories(self):
        r = json.loads(Path("data/exact-witness-participation.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_minimum_cover_participation_measured")
        self.assertEqual((s["world_count"], s["backbone_count"], s["optional_optimal_count"], s["never_optimal_count"]), (1964, 62, 1852, 50))
        self.assertEqual((s["total_participation"], s["backbone_participation"], s["optional_participation"]), ("188", "62", "126"))
        self.assertEqual((s["substitution_component_mass"], s["kernel_mass"]), ("120", "10"))
        self.assertTrue(s["all_optional_strictly_between"])
        self.assertTrue(s["never_zero"])
        self.assertTrue(s["backbone_one"])
        self.assertTrue(s["substitution_formula_verified"])
        self.assertEqual(s["substitution_world_count"], 1770)
        self.assertEqual(s["kernel_local_mass_checks"], {"8": "3", "11": "3", "12": "1", "21": "2", "45": "1"})
        self.assertEqual(s["optional_min"], "4/451")
        self.assertEqual(s["optional_max"], "1/2")


if __name__ == "__main__":
    unittest.main()
