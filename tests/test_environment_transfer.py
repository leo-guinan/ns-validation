import json
import unittest
from pathlib import Path


class TransferTests(unittest.TestCase):
    def test_direct_elaborated_dependencies_are_separate_from_cone(self):
        receipt = json.loads(Path("data/environment-transfer.json").read_text())
        self.assertEqual(receipt["elaborated_direct_dependencies"]["count"], 2)
        self.assertEqual(len(receipt["elaborated_direct_dependencies"]["declarations"]), 2)
        self.assertIsNone(receipt["transitive_cone"])
        self.assertTrue(receipt["target_elaboration"]["target_olean_produced"])
        self.assertTrue(receipt["immediate_recheck"]["target_olean_produced"])


if __name__ == "__main__":
    unittest.main()
