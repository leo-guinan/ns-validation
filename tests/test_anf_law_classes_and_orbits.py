import json
import unittest
from pathlib import Path


class AnfLawClassesAndOrbitsTests(unittest.TestCase):
    def test_classes_closure_and_orbits(self):
        r = json.loads(Path("data/anf-law-classes-and-orbits.json").read_text())
        self.assertEqual(r["status"], "exact_anf_class_and_orbit_structure_measured")
        self.assertEqual([(x["component_index"], x["anf_function_class_count"], x["xor_closure_of_nonzero_functions"], x["defect_state_orbit_count"], x["violation_predicate_orbit_count"]) for x in r["components"]], [(8, 3, False, 3, 2), (11, 15, False, 10, 9)])
        self.assertTrue(all(x["all_functions_share_full_term"] for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
