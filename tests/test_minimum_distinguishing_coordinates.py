import json
import unittest
from pathlib import Path


class MinimumDistinguishingCoordinatesTests(unittest.TestCase):
    def test_exact_minima_and_replay_verification(self):
        r = json.loads(Path("data/minimum-distinguishing-coordinates.json").read_text())
        self.assertEqual(r["status"], "exact_minimum_distinguishing_coordinates_measured")
        self.assertEqual(r["audit"]["raw_state_pair_count"], 2502)
        self.assertTrue(r["audit"]["counts_reconciled"])
        self.assertEqual(r["coordinate_identity_audit"]["experiment42_optional_shell_size"], 200)
        self.assertTrue(r["coordinate_identity_audit"]["removal_coordinates_equal_optional_shell"])
        self.assertTrue(r["coordinate_identity_audit"]["addition_coordinates_equal_optional_shell"])
        for k in ("removal", "addition"):
            self.assertEqual(r[k]["minimum_dimension"], 200)
            self.assertEqual(r[k]["raw_state_pair_count"], 2502)
            self.assertEqual(r[k]["pair_constraints"], 2502)
            self.assertTrue(r[k]["verified"])
            self.assertTrue(r[k]["all_coordinates_singleton_certified"])
            self.assertIn("Optimal", r[k]["solver_status"])
            self.assertEqual(len(r[k]["chosen_coordinates"]), 200)


if __name__ == "__main__":
    unittest.main()
