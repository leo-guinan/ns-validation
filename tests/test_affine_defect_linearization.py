import json
import unittest
from pathlib import Path


class AffineDefectLinearizationTests(unittest.TestCase):
    def test_translated_closure_is_falsified(self):
        r = json.loads(Path("data/affine-defect-linearization.json").read_text())
        self.assertEqual(r["status"], "exact_affine_defect_linearization_measured")
        self.assertEqual([(x["component_index"], x["zero_and_masks_size"], x["translated_mask_xor_closed"], x["gf2_dimension"], x["h_bijective"]) for x in r["components"]], [(8, 3, False, 2, None), (11, 15, False, 14, None)])
        self.assertTrue(all(x["unique_nonzero_coefficients"] for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
