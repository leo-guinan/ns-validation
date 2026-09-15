import json
import unittest
from pathlib import Path


class ActivationTests(unittest.TestCase):
    def test_incomplete_runs_do_not_claim_activation_ratio(self):
        receipt = json.loads(Path("data/activation-experiment.json").read_text())
        self.assertEqual(receipt["status"], "measured_activation_not_elaboration")
        self.assertIsNone(receipt["activation_ratio"])
        self.assertTrue(all(not item["target_olean_produced"] for item in receipt["conditions"]))
        self.assertIsNone(receipt["cone"])


if __name__ == "__main__":
    unittest.main()
