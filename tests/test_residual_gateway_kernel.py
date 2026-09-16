import json
import unittest
from pathlib import Path


class ResidualGatewayKernelTests(unittest.TestCase):
    def test_forced_coverage_and_residual_bounds_are_separate(self):
        receipt = json.loads(Path("data/residual-gateway-kernel.json").read_text())
        self.assertEqual(receipt["experiment"], "20-residual-gateway-kernel")
        self.assertEqual(receipt["summary"]["residual_frontier_counts"], [0, 0, 126, 126, 126, 139])
        self.assertEqual(receipt["summary"]["total_lower_bounds"], [12, 12, 293, 293, 293, 297])
        self.assertEqual(receipt["summary"]["total_upper_bounds"], [12, 12, 304, 304, 304, 313])
        self.assertIn("No semantic necessity", receipt["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
