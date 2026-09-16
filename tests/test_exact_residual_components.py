import json
import unittest
from pathlib import Path


class ExactResidualComponentTests(unittest.TestCase):
    def test_all_components_are_exactly_solved(self):
        receipt = json.loads(Path("data/exact-residual-components.json").read_text())
        self.assertEqual(receipt["experiment"], "21-exact-residual-component-solve")
        self.assertTrue(receipt["summary"]["all_components_exact"])
        self.assertEqual(receipt["summary"]["exact_total_covers"], [12, 12, 302, 302, 302, 309])
        self.assertEqual(receipt["summary"]["component_counts"], [0, 0, 54, 54, 54, 53])
        self.assertEqual(receipt["summary"]["signature_class_count"], 13)


if __name__ == "__main__":
    unittest.main()
