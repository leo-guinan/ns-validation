import json
import unittest
from pathlib import Path


class Experiment41WitnessProvenanceTests(unittest.TestCase):
    def test_baseline_provenance_is_explicitly_unrecovered(self):
        receipt = json.loads(Path("data/experiment41-witness-provenance.json").read_text())
        self.assertEqual(receipt["status"], "exp33_baseline_witness_unrecovered")
        self.assertEqual(receipt["witnesses"]["current_stored_I2508"]["width"], 309)
        self.assertFalse(receipt["witnesses"]["current_stored_I2508"]["tensorDiff_divergence"])
        self.assertTrue(receipt["witnesses"]["current_stored_I2508"]["weak_pressure_poisson"])
        self.assertIsNone(receipt["witnesses"]["Exp33_swept_baseline"]["identity_hash"])
        self.assertFalse(receipt["reconciliation"]["stored_nonbackbone_equals_exp33_feasible_forbidden"])


if __name__ == "__main__":
    unittest.main()
