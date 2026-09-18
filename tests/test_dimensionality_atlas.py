import json
import unittest
from pathlib import Path


class DimensionalityAtlasTests(unittest.TestCase):
    def test_global_unions_covers_and_reversal(self):
        r = json.loads(Path("data/dimensionality-atlas.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_local_global_dimensionality_incidence_measured")
        self.assertEqual(s["optional_shell_size"], 200)
        self.assertEqual(s["removal_backbone_union_size"], 200)
        self.assertEqual(s["addition_backbone_union_size"], 200)
        self.assertEqual(s["counting_lower_bound_worlds"], 67)
        self.assertEqual(r["removal_world_cover"]["minimum_world_count"], 188)
        self.assertEqual(r["addition_world_cover"]["minimum_world_count"], 188)
        self.assertTrue(r["removal_world_cover"]["verified"])
        self.assertTrue(r["addition_world_cover"]["verified"])
        self.assertEqual(s["removal_reversal_family_equal_pairs"], 1964)
        self.assertEqual(s["reversal_family_mismatch_count"], 0)


if __name__ == "__main__":
    unittest.main()
