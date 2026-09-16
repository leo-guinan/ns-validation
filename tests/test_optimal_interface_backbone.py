import json
import unittest
from pathlib import Path


class OptimalInterfaceBackboneTests(unittest.TestCase):
    def test_optimal_interfaces_are_rigid_in_measured_graph(self):
        receipt = json.loads(Path("data/optimal-interface-backbone.json").read_text())
        self.assertEqual(receipt["experiment"], "22-optimal-interface-backbone")
        self.assertTrue(receipt["summary"]["all_components_exact"])
        self.assertEqual(receipt["summary"]["exact_total_covers"], [12, 12, 302, 302, 302, 309])
        self.assertEqual(receipt["summary"]["optimal_interface_counts"], [1, 1, 1, 1, 1, 1])
        self.assertEqual(receipt["summary"]["additional_residual_backbone_counts"], [0, 0, 63, 63, 63, 65])


if __name__ == "__main__":
    unittest.main()
