import json
import unittest
from pathlib import Path


class ExactFlexibleShellTests(unittest.TestCase):
    def test_candidate_partition_and_support(self):
        r = json.loads(Path("data/exact-flexible-shell.json").read_text())
        self.assertEqual(r["status"], "exact_component_support_measured")
        self.assertEqual(r["candidate_universe"], {"total": 915, "basis_touching": 472, "basis_disconnected": 443, "basis_touching_but_never_optimal": 22})
        self.assertEqual(r["optimum_support"]["backbone_size"], 250)
        self.assertEqual(r["optimum_support"]["support_size"], 450)
        self.assertEqual(r["optimum_support"]["flexible_shell_size"], 200)
        self.assertEqual(r["factorization"]["sum_widths"], 309)
        self.assertEqual(r["factorization"]["sum_slack"], 11)
        self.assertEqual(r["factorization"]["positive_slack_factor"], 750)
        self.assertEqual(r["factorization"]["zero_slack_substitution_factor"], 2470259125792014336000)


if __name__ == "__main__":
    unittest.main()
