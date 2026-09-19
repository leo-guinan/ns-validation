import json
import unittest
from pathlib import Path


class MinimumCompatibilityRepairTests(unittest.TestCase):
    def test_repairs_and_same_signature_witnesses(self):
        r = json.loads(Path("data/minimum-compatibility-repair.json").read_text())
        self.assertEqual(r["status"], "exact_minimum_compatibility_repair_measured")
        self.assertEqual([(x["component_index"], x["minimum_repair_size"], x["minimum_repair_count"], x["repaired_reconstruction_equal"], x["same_signature_witness_found"]) for x in r["components"]], [(8, 2, 1, True, True), (11, 4, 1, True, True)])
        self.assertTrue(all(x["false_positive_count"] > 0 for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
