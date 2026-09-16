import json
import unittest
from pathlib import Path


class GatewayNecessityTests(unittest.TestCase):
    def test_small_cases_have_matching_exact_bounds(self):
        receipt = json.loads(Path("data/gateway-necessity.json").read_text())
        self.assertEqual(receipt["experiment"], "19-gateway-necessity")
        self.assertEqual(receipt["summary"]["forced_local_counts"][:2], [12, 12])
        self.assertEqual(receipt["summary"]["lower_bounds"][:2], [12, 12])
        self.assertEqual(receipt["summary"]["greedy_upper_bounds"][:2], [12, 12])
        self.assertEqual(receipt["summary"]["exact_values"][:2], [12, 12])
        self.assertEqual(receipt["summary"]["exact_values"][2:], [None, None, None, None])


if __name__ == "__main__":
    unittest.main()
