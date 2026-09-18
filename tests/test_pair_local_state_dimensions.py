import json
import unittest
from pathlib import Path


class PairLocalStateDimensionsTests(unittest.TestCase):
    def test_local_dimensions_and_symmetry(self):
        r = json.loads(Path("data/pair-local-state-dimensions.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_pair_local_dimensions_measured")
        self.assertEqual(s["ordered_pair_count"], 1964)
        self.assertEqual(s["max_m_R"], 3)
        self.assertEqual(s["max_m_A"], 3)
        self.assertEqual(s["pairs_m_R_equals_m_A"], 1964)
        self.assertEqual(s["pairs_m_R_not_m_A"], 0)
        self.assertEqual(s["I_distribution"], {"1": 1888, "2": 58, "3": 18})
        self.assertEqual(s["m_R_distribution"], {"1": 1888, "2": 58, "3": 18})
        self.assertEqual(s["m_A_distribution"], {"1": 1888, "2": 58, "3": 18})
        self.assertTrue(all(p["minimum_R_solution_count"] >= 1 and p["minimum_A_solution_count"] >= 1 for p in r["pairs"]))


if __name__ == "__main__":
    unittest.main()
