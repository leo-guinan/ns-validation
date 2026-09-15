import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation import graph_edges, load_proof_graph, render_proof_graph_report


class ProofGraphTests(unittest.TestCase):
    def test_outline_graph_has_explicit_nodes_and_literal_edges(self):
        root = Path(__file__).resolve().parents[1]
        graph = load_proof_graph(root / "data/proof-interface-graph.json")
        self.assertEqual(graph["status"], "outline_only")
        self.assertEqual(len(graph["nodes"]), 6)
        self.assertEqual(len(graph_edges(graph)), 5)
        self.assertTrue(all(node["exported_object"] for node in graph["nodes"]))
        self.assertTrue(all(edge["literal_interface"] for edge in graph["edges"]))
        self.assertIn("minimal sufficient interface", graph["not_yet_measured"])

    def test_unknown_edge_endpoint_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "graph.json"
            path.write_text(json.dumps({
                "status": "outline_only",
                "nodes": [{"id":"a","name":"A","assumptions":[],"internal_construction":"x","exported_object":"x","validation_condition":"x","source_refs":[]}],
                "edges": [{"from":"a","to":"missing","literal_interface":"x","source_refs":[]}],
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown node"):
                load_proof_graph(path)

    def test_report_preserves_evidence_boundary(self):
        root = Path(__file__).resolve().parents[1]
        report = render_proof_graph_report(load_proof_graph(root / "data/proof-interface-graph.json"))
        self.assertIn("Status: outline_only", report)
        self.assertIn("complete 166-page proof artifact was not available", report)
        self.assertIn("Not yet measured", report)


if __name__ == "__main__":
    unittest.main()
