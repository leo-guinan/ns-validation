import json
import unittest
from pathlib import Path


class ContinuationStateSufficiencyTests(unittest.TestCase):
    def test_cross_tab_and_compression_sufficiency(self):
        r = json.loads(Path("data/continuation-state-sufficiency.json").read_text())
        self.assertEqual(r["status"], "exact_continuation_signatures_measured")
        self.assertEqual(r["cross_tab"], {"precedence_pairs": 34, "partial_retention_pairs": 76, "nonposet_pairs": 12, "precedence_and_partial": 34, "precedence_not_partial": 0, "partial_not_precedence": 42, "nonposet_and_precedence": 6, "nonposet_and_partial": 12, "all_three": 6})
        s = r["summary"]
        self.assertEqual(s["ordered_pair_count"], 1964)
        self.assertEqual(s["pairs_with_depth_collision"], 54)
        self.assertEqual(s["pairs_with_removal_collision"], 0)
        self.assertEqual(s["pairs_with_addition_collision"], 0)
        self.assertEqual(s["pairs_with_full_RA_collision"], 0)
        self.assertEqual(s["total_continuation_states"], 4104)
        self.assertEqual(s["total_continuation_equivalence_classes"], 4104)
        self.assertEqual(r["continuation_state_complexity"]["K_continuation"], 4104)
        self.assertEqual(r["continuation_state_complexity"]["arbitrary_index_lower_bound_bits"], 13)
        self.assertEqual(r["projection_universes"]["removal_count"], 4104)
        self.assertEqual(r["projection_universes"]["addition_count"], 4104)
        self.assertTrue(r["projection_universes"]["bijection_verified"])
        self.assertIn("depth", r["collision_witnesses"])


if __name__ == "__main__":
    unittest.main()
