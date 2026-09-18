import json
import unittest
from pathlib import Path


class SurvivalAttackIncidenceTests(unittest.TestCase):
    def test_ordering_and_containment(self):
        r = json.loads(Path("data/survival-attack-incidence.json").read_text())
        self.assertEqual(r["status"], "exact_survival_attack_incidence_measured")
        self.assertEqual([(x["component_index"], len(x["pairwise_inversions"]["p_vs_q_tau"]), len(x["pairwise_inversions"]["p_vs_q_kappa"])) for x in r["components"]], [(8, 0, 12), (11, 0, 412), (12, 0, 0), (21, 0, 0), (45, 0, 0)])
        self.assertTrue(all(x["all_feasibility_blockers_are_optimality_blockers"] for x in r["components"]))
        self.assertTrue(r["exact_one_summary"]["all_components_verified"])
        self.assertTrue(all(x["all_minimum_feasibility_neighborhoods_are_exact_one_cuts"] for x in r["components"]))
        self.assertTrue(all(all(y["contained_minimum_optimality_blockers"] is not None for y in x["feasibility_to_optimality_containment"]) for x in r["components"]))


if __name__ == "__main__":
    unittest.main()
