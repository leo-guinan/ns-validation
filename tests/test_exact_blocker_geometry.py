import json
import unittest
from pathlib import Path


class ExactBlockerGeometryTests(unittest.TestCase):
    def test_blocker_families_are_complete(self):
        r = json.loads(Path("data/exact-blocker-geometry.json").read_text())
        self.assertEqual(r["status"], "exact_minimum_blocker_geometry_measured")
        self.assertEqual([(x["component_index"], x["table"]["tau"], x["table"]["minimum_optimality_blocker_count"], x["table"]["kappa"], x["table"]["minimum_feasibility_blocker_count"], x["optimality_blockers"]["complete"]) for x in r["components"]], [(8, 4, 3, 4, 1, True), (11, 16, 5, 21, 2, True), (12, 1, 1, 2, 2, True), (21, 1, 2, 4, 2, True), (45, 1, 1, 2, 2, True)])
        self.assertTrue(all(x["feasibility_blockers"]["complete"] and x["feasibility_identity_verified"] for x in r["components"]))
        self.assertTrue(r["duality_checks"]["singleton_union_matches_residual_backbone"])
        self.assertTrue(r["duality_checks"]["feasibility_identity_verified"])
        self.assertTrue(all(x["participation_comparison"] for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
