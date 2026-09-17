import json
import unittest
from pathlib import Path


class ScopeEffectUnderFixedContractTests(unittest.TestCase):
    def test_only_frontier_scope_changes(self):
        receipt = json.loads(Path("data/scope-effect-under-fixed-contract.json").read_text())
        self.assertEqual(receipt["status"], "exact_scope_effect_measured")
        full = receipt["contracts"]["full"]
        delta = receipt["contracts"]["delta_B_to_T"]
        self.assertEqual(full["minimum_cover_width"], 309)
        self.assertEqual(delta["minimum_cover_width"], 309)
        self.assertEqual(full["fingerprint"]["h_L"], delta["fingerprint"]["h_L"])
        self.assertEqual(full["fingerprint"]["h_O"], delta["fingerprint"]["h_O"])
        self.assertEqual(full["fingerprint"]["h_K"], delta["fingerprint"]["h_K"])
        self.assertEqual(receipt["known_optima_probe"]["I2508"]["delta_coverage"], 2508)
        self.assertEqual(receipt["known_optima_probe"]["J_full"]["delta_coverage"], 2508)
        self.assertTrue(receipt["known_optima_probe"]["J_full"]["admissible"])


if __name__ == "__main__":
    unittest.main()
