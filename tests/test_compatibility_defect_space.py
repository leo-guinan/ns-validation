import json
import unittest
from pathlib import Path


class CompatibilityDefectSpaceTests(unittest.TestCase):
    def test_boolean_space(self):
        r = json.loads(Path("data/compatibility-defect-space.json").read_text())
        self.assertEqual(r["status"], "exact_boolean_compatibility_defect_space_measured")
        self.assertEqual([(x["component_index"], x["repair_dimension"], x["all_nonzero_vectors_realized"], x["defect_determines_violation_signature"], x["zero_defect_equals_opt"]) for x in r["components"]], [(8, 2, True, True, True), (11, 4, True, True, True)])
        self.assertEqual(sum(json.loads(Path("data/compatibility-defect-space.json").read_text())["components"][0]["defect_vector_multiplicities"].values()), 144)
        self.assertEqual(sum(json.loads(Path("data/compatibility-defect-space.json").read_text())["components"][1]["defect_vector_multiplicities"].values()), 10584)


if __name__ == "__main__":
    unittest.main()
