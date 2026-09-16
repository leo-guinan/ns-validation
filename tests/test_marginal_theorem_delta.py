import json
import unittest
from pathlib import Path


class MarginalTheoremDeltaTests(unittest.TestCase):
    def test_exact_containment_and_direct_consumption(self):
        receipt = json.loads(Path("data/marginal-theorem-delta.json").read_text())
        accounting = receipt["support_accounting"]
        self.assertEqual(accounting["A_minus_B"], [])
        self.assertEqual(accounting["B_minus_A"], [
            "NavierStokesR3.ProblemStatement.breakdownStatement",
            "NavierStokesR3.theorem_1_1",
        ])
        self.assertEqual(receipt["marginal_support"]["size"], 2)
        self.assertTrue(receipt["dependency_test"]["final_directly_references_initial_rest"])
        self.assertEqual(receipt["warm_measurements"]["module_recheck"]["bytes_changed"], 0)


if __name__ == "__main__":
    unittest.main()
