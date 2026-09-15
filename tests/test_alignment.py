import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation.alignment import build_source_scan


class AlignmentTests(unittest.TestCase):
    def test_source_scan_is_not_claimed_as_elaborated(self):
        payload = build_source_scan(Path("/tmp/NavierStokesAndEuler"), ["NavierStokes/R3/Theorem.lean"])
        self.assertEqual(payload["status"], "syntax_inventory_not_elaborated")
        self.assertGreater(len(payload["nodes"]), 0)
        self.assertTrue(all("/tmp/" not in node["file"] for node in payload["nodes"]))

    def test_falsifier_receipt_is_explicit(self):
        payload = json.loads(Path("data/interface-alignment.json").read_text())
        self.assertEqual(payload["falsifier"]["result"], "triggered")
        self.assertEqual(len(payload["proof_nodes"]), 7)
        self.assertEqual(len(payload["interfaces"]), 6)


if __name__ == "__main__":
    unittest.main()
