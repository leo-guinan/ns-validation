import json
import unittest
from pathlib import Path


class MinimumDirectObservabilityTests(unittest.TestCase):
    def test_minimum_interfaces(self):
        r = json.loads(Path("data/minimum-direct-observability.json").read_text())
        self.assertEqual(r["status"], "exact_minimum_direct_observability_measured")
        self.assertEqual([(x["component_index"], x["minimum_observation_size"], x["minimum_observation_set_count"], x["all_inverse_decoders_linear"], x["all_inverse_decoders_affine"]) for x in r["components"]], [(8, 3, 1, True, True), (11, 15, 1, True, True)])
        self.assertEqual([len(x["observation_backbone"]) for x in r["components"]], [3, 15])


if __name__ == "__main__":
    unittest.main()
