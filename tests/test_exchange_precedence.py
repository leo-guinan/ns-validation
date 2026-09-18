import json
import unittest
from pathlib import Path


class ExchangePrecedenceTests(unittest.TestCase):
    def test_precedence_is_rare_but_explicit(self):
        r = json.loads(Path("data/exchange-precedence.json").read_text())
        self.assertEqual(r["status"], "exact_exchange_precedence_measured")
        self.assertEqual(r["summary"]["component_count"], 302)
        self.assertEqual(r["summary"]["ordered_pair_count"], 1964)
        self.assertEqual(r["summary"]["pairs_with_precedence"], 34)
        self.assertEqual(r["summary"]["maximum_precedence_depth"], 3)
        self.assertTrue(r["summary"]["all_geodesic_paths_distance_decreasing"])
        w = r["component_9_precedence_witness"]
        self.assertEqual(w["direct_distance"], 2)
        self.assertEqual(w["geodesic_count"], 1)
        self.assertEqual(w["earliest_removal_step"]["NavierStokesR3.ComparisonCutoffs.baseCutoff_iteratedFDeriv_le"], 2)
        self.assertEqual(len(w["exchange_steps"]), 2)
        self.assertEqual(w["exchange_steps"][0]["add"], "NavierStokesR3.LocalizedFluxEstimates.weightSecondDerivativeConstant_pos")
        self.assertEqual(w["state_sizes"], {"S": 2, "S1": 2, "T": 2})
        self.assertTrue(all(len(v) == 64 for v in w["state_hashes"].values()))


if __name__ == "__main__":
    unittest.main()
