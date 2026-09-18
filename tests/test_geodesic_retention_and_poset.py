import json
import unittest
from pathlib import Path


class GeodesicRetentionAndPosetTests(unittest.TestCase):
    def test_retention_convexity_and_poset_results(self):
        r = json.loads(Path("data/geodesic-retention-and-poset-test.json").read_text())
        s = r["summary"]
        self.assertEqual(r["status"], "exact_geodesic_retention_measured")
        self.assertEqual(s["ordered_pair_count"], 1964)
        self.assertEqual(s["full_retention_pairs"], 1888)
        self.assertEqual(s["partial_retention_pairs"], 76)
        self.assertFalse(s["geodesically_convex"])
        self.assertFalse(s["all_geodesic_pairs_poset_exact"])
        self.assertEqual(s["pairs_not_poset_exact"], 12)
        self.assertIn("ordered remove/add pair", r["poset_event_encoding"])
        self.assertEqual(r["component_9_reference"]["retention_fraction"], "1/4")
        self.assertEqual(r["poset_counterexample"]["component"], 31)


if __name__ == "__main__":
    unittest.main()
