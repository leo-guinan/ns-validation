import json
import unittest
from pathlib import Path


class DefectLogicTests(unittest.TestCase):
    def test_logic_and_symmetry(self):
        r = json.loads(Path("data/defect-logic.json").read_text())
        self.assertEqual(r["status"], "exact_defect_logic_measured")
        self.assertEqual([(x["component_index"], x["monotone_violation_map"], x["dependency_order_distribution"]) for x in r["components"]], [(8, False, {"2": 3}), (11, False, {"4": 15})])
        self.assertFalse(r["components"][0]["multiplicity_factorization"]["independent_2x2_test"])
        self.assertTrue(r["components"][1]["reversal_test"]["multiplicity_invariant"])
        self.assertTrue(r["components"][1]["reversal_test"]["function_multiset_invariant"])


if __name__ == "__main__":
    unittest.main()
