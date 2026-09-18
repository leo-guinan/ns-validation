import json
import unittest
from pathlib import Path


class CoverGapIncidenceDecompositionTests(unittest.TestCase):
    def test_forced_plus_residual_cover(self):
        r = json.loads(Path("data/cover-gap-incidence-decomposition.json").read_text())
        self.assertEqual(r["status"], "exact_backbone_incidence_decomposition_measured")
        for k in ("removal", "addition"):
            x = r[k]
            self.assertEqual(x["private_coordinate_count"], 58)
            self.assertEqual(x["forced_world_count"], 58)
            self.assertEqual(x["forced_backbone_union_size"], 58)
            self.assertTrue(x["all_forced_world_backbones_singleton"])
            self.assertEqual(x["residual_coordinate_count"], 142)
            self.assertEqual(x["residual_world_cover_count"], 130)
            self.assertEqual(x["forced_plus_residual"], 188)
            self.assertTrue(x["residual_cover_verified"])
            self.assertEqual(x["necessity_degree_histogram"]["1"], 58)


if __name__ == "__main__":
    unittest.main()
