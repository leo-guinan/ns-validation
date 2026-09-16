import json
import unittest
from pathlib import Path


class ActiveFrontierReuseTests(unittest.TestCase):
    def test_persistence_is_separated_from_active_reuse(self):
        receipt = json.loads(Path("data/active-frontier-reuse.json").read_text())
        self.assertEqual(receipt["experiment"], "16-active-frontier-reuse")
        self.assertEqual(receipt["summary"]["downstream_transition_observations"], 5)
        self.assertEqual(receipt["summary"]["D_nonzero_count"], 0)
        self.assertEqual(receipt["summary"]["T_nonzero_count"], 0)
        self.assertIn("inherited availability", receipt["interpretation_boundary"])


if __name__ == "__main__":
    unittest.main()
