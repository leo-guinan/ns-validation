import json
import unittest
from pathlib import Path


class CoverChoiceClassificationTests(unittest.TestCase):
    def test_kernel_multiplicity_and_reversal(self):
        r = json.loads(Path("data/cover-choice-classification.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_component_cover_choice_measured")
        self.assertEqual(s["component_count"], 125)
        self.assertEqual(s["kernel_component_count"], 5)
        self.assertEqual(s["kernel_saving_sum"], 12)
        self.assertEqual(s["global_residual_width"], 130)
        self.assertEqual(s["residual_backbone_size"], 4)
        self.assertEqual(s["residual_support_size"], 1856)
        self.assertTrue(s["reversal_component_correspondence_verified"])
        self.assertEqual(s["classification_counts"], {"no_saving_unique": 0, "no_saving_multiple": 120, "saving_unique": 3, "saving_multiple": 2})
        d = r["derived_classification"]
        self.assertTrue(d["zero_saving_width_one_all"])
        self.assertTrue(d["zero_saving_coordinate_one_all"])
        self.assertTrue(d["zero_saving_multiple_all"])
        self.assertEqual(d["residual_candidate_world_count"], 1906)
        self.assertEqual(d["residual_backbone_count"], 4)
        self.assertEqual(d["residual_optional_optimal_count"], 1852)
        self.assertEqual(d["residual_never_optimal_count"], 50)
        self.assertTrue(d["residual_partition_exact"])
        self.assertTrue(d["residual_never_optimal_in_kernel"])
        self.assertEqual(d["full_backbone_count"], 62)
        self.assertTrue(d["full_partition_exact"])


if __name__ == "__main__":
    unittest.main()
