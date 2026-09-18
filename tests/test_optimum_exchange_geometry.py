import json
import unittest
from pathlib import Path


class OptimumExchangeGeometryTests(unittest.TestCase):
    def test_global_exchange_connectivity_and_diameter(self):
        r = json.loads(Path("data/optimum-exchange-geometry.json").read_text())
        self.assertEqual(r["status"], "exact_component_exchange_geometry_measured")
        self.assertEqual(r["summary"]["component_count"], 302)
        self.assertTrue(r["summary"]["all_local_exchange_graphs_connected"])
        self.assertTrue(r["summary"]["global_exchange_graph_connected"])
        self.assertEqual(r["summary"]["disconnected_component_count"], 0)
        self.assertEqual(r["summary"]["global_diameter"], 59)
        self.assertEqual(r["summary"]["total_local_exchange_edges"], 944)
        self.assertTrue(all(c["connected"] for c in r["components"]))


if __name__ == "__main__":
    unittest.main()
