import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation import load_stages, stage_edges


class StageModelTests(unittest.TestCase):
    def test_case_study_stage_graph_is_explicit_and_connected(self):
        root = Path(__file__).resolve().parents[1]
        stages = load_stages(root / "data" / "proof-stages.json")
        self.assertEqual([stage.id for stage in stages], [
            "search", "candidate-insight", "proof-construction",
            "formalization", "kernel-verification", "reuse",
        ])
        self.assertEqual(len(stage_edges(stages)), 5)
        self.assertTrue(all(stage.work and stage.state_exported for stage in stages))

    def test_schema_and_evidence_are_valid_json(self):
        root = Path(__file__).resolve().parents[1]
        for path in [
            root / "schemas" / "stage.schema.json",
            root / "schemas" / "evidence.schema.json",
            root / "data" / "source-ledger.json",
            root / "data" / "cost-estimates.json",
        ]:
            with self.subTest(path=path):
                json.loads(path.read_text(encoding="utf-8"))

    def test_unknown_predecessor_is_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "stages.json"
            path.write_text(json.dumps([{
                "id": "b", "name": "B", "predecessors": ["missing"],
                "work": "unknown", "state_exported": "unknown",
                "verification_burden": "unknown", "trust_assumptions": [],
            }]), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown predecessor"):
                load_stages(path)


if __name__ == "__main__":
    unittest.main()
