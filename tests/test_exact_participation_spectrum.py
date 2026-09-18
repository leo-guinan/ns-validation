import json
import unittest
from pathlib import Path


class ExactParticipationSpectrumTests(unittest.TestCase):
    def test_exact_partition_and_conservation(self):
        r = json.loads(Path("data/exact-participation-spectrum.json").read_text())
        self.assertEqual(r["status"], "exact_component_participation_measured")
        self.assertEqual(r["candidate_classes"], {"backbone": 250, "optional_optimal": 200, "basis_disconnected": 443, "basis_touching_never_optimal": 22})
        self.assertEqual(r["checksum"], {"sum_participation": "309", "backbone_sum": "250", "optional_shell_sum": "59", "exact_verified": True})
        self.assertEqual(r["spectrum"]["mean_optional_participation"], "59/200")
        self.assertEqual(r["spectrum"]["mean_optional_participation_decimal"], 0.295)
        self.assertFalse(r["spectrum"]["uniformity_claim"])
        self.assertEqual(r["spectrum"]["optional_fraction_min"], "1/37")
        self.assertEqual(r["spectrum"]["optional_fraction_max"], "4/5")
        for v in r["candidates"].values():
            if v["class"] == "backbone":
                self.assertEqual(v["numerator"], v["denominator"])
            elif v["class"] == "optional_optimal":
                self.assertGreater(v["numerator"], 0)
                self.assertLess(v["numerator"], v["denominator"])
            else:
                self.assertEqual(v["numerator"], 0)


if __name__ == "__main__":
    unittest.main()
