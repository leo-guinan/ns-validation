import json
import unittest
from pathlib import Path


class LowerOrderParityCheckTests(unittest.TestCase):
    def test_unique_constant_term_check(self):
        r = json.loads(Path("data/lower-order-parity-check.json").read_text())
        self.assertEqual(r["status"], "exact_lower_order_parity_check_measured")
        self.assertEqual([(x["component_index"], x["full_lower_order_dimension"], x["mask_span_dimension"], x["parity_check_support"], x["unique_nonzero_parity_check"], x["reversal_invariant"]) for x in r["components"]], [(8, 3, 2, ["00"], True, True), (11, 15, 14, ["0000"], True, True)])
        self.assertTrue(all(x["all_masks_annihilated"] and x["affine_independent_nonzero_masks"] for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
