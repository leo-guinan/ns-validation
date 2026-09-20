import json
import unittest
from pathlib import Path


class BooleanDefectStructureTests(unittest.TestCase):
    def test_degrees_edges_and_automorphisms(self):
        r = json.loads(Path("data/boolean-defect-structure.json").read_text())
        self.assertEqual(r["status"], "exact_boolean_defect_structure_measured")
        self.assertEqual([(x["component_index"], x["degree_histogram"], x["transition_class_counts"], x["global_reversal_automorphism"]["exists"], x["global_reversal_automorphism"]["certificate_verified"]) for x in r["components"]], [(8, {"2": 3}, {"pure-add": 2, "replacement": 2}, True, True), (11, {"4": 15}, {"pure-add": 4, "replacement": 28}, True, True)])
        self.assertTrue(all(not x["transition_class_counts"].get("pure-remove", 0) for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
