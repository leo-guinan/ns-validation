import json
import unittest
from pathlib import Path


class ConstraintSubsumptionAnalysisTests(unittest.TestCase):
    def test_basis_is_exact_and_inherited_certificates_exist(self):
        receipt = json.loads(Path("data/constraint-subsumption-analysis.json").read_text())
        self.assertEqual(receipt["status"], "exact_neighborhood_basis_measured")
        self.assertEqual(receipt["counts"]["frontier_identities"], 2522)
        self.assertEqual(receipt["counts"]["unique_neighborhoods"], 1662)
        self.assertEqual(receipt["counts"]["inclusion_minimal_basis_classes"], 320)
        self.assertEqual(receipt["counts"]["removal_decomposition"]["strict_subsumption_removals"] + receipt["counts"]["removal_decomposition"]["duplicate_minimal_class_removals"], 2202)
        self.assertEqual(len(receipt["inherited_certificates"]), 14)
        self.assertTrue(all(x["witness"] for x in receipt["inherited_certificates"].values()))
        self.assertTrue(receipt["basis_verification"]["frontier_constraints_equivalent_to_basis"])
        self.assertTrue(receipt["basis_verification"]["basis_classes_have_no_strictly_smaller_class"])


if __name__ == "__main__":
    unittest.main()
