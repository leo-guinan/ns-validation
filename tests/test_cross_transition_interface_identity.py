import json
import unittest
from pathlib import Path


class CrossTransitionInterfaceIdentityTests(unittest.TestCase):
    def test_equal_width_identity_and_containment_are_separate(self):
        receipt = json.loads(Path("data/cross-transition-interface-identity.json").read_text())
        self.assertEqual(receipt["experiment"], "23-cross-transition-interface-identity")
        self.assertTrue(receipt["summary"]["three_2436_optima_identical"])
        self.assertFalse(receipt["summary"]["any_2436_contained_in_2508"])
        self.assertTrue(receipt["summary"]["72_subset_2508"])
        self.assertFalse(receipt["summary"]["2508_subset_72"])
        self.assertEqual(receipt["summary"]["2436_vs_2508_symmetric_difference"], 25)
        self.assertEqual(receipt["summary"]["2436_vs_2508_net_width_change"], 7)
        self.assertEqual(receipt["summary"]["optimal_sizes"], [12, 12, 302, 302, 302, 309])
        self.assertEqual(receipt["summary"]["identical_optimal_pairs"], 4)


if __name__ == "__main__":
    unittest.main()
