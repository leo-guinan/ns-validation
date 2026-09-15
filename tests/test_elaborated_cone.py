import json
import unittest
from pathlib import Path


class ConeReceiptTests(unittest.TestCase):
    def test_blocked_attempt_does_not_claim_a_cone(self):
        receipt = json.loads(Path("data/elaborated-cone.json").read_text())
        self.assertEqual(receipt["status"], "blocked_before_elaboration")
        self.assertIsNone(receipt["cone"])
        self.assertIsNone(receipt["direct_dependencies"])
        self.assertFalse(receipt["attempt"]["theorem_olean_produced"])


if __name__ == "__main__":
    unittest.main()
