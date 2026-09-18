import json
import unittest
from pathlib import Path


class ExactDegradationProfilesTests(unittest.TestCase):
    def test_kernel_transition_thresholds(self):
        r = json.loads(Path("data/exact-degradation-profiles.json").read_text())
        self.assertEqual(r["status"], "exact_adversarial_degradation_profiles_measured")
        profiles = {x["component_index"]: x for x in r["kernel_profiles"]}
        def thresholds(i):
            return [(x["target_width"], x["threshold"]) for x in profiles[i]["transitions"]]
        self.assertEqual(thresholds(8), [(4, 4), (5, 4), ("infinity", 4)])
        self.assertEqual(thresholds(11), [(4, 16), (5, 21), (6, 21), (7, 21), ("infinity", 21)])
        self.assertEqual(thresholds(12), [(2, 1), ("infinity", 2)])
        self.assertEqual(thresholds(21), [(3, 1), (4, 4), (5, 4), (6, 4), ("infinity", 4)])
        self.assertEqual(thresholds(45), [(2, 1), ("infinity", 2)])
        self.assertTrue(all(t["verified"] for x in r["kernel_profiles"] for t in x["transitions"]))
        self.assertEqual({x["component_index"]: x["adversarial_profile"]["infinity_from_budget"] for x in r["kernel_profiles"]}, {8: 4, 11: 21, 12: 2, 21: 4, 45: 2})
        self.assertEqual([(x["component_index"], x["budget"]) for x in r["same_budget_feasible_and_infeasible"]], [(8, 4), (21, 4)])


if __name__ == "__main__":
    unittest.main()
