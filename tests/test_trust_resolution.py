import json
import unittest
from pathlib import Path


class TrustResolutionTests(unittest.TestCase):
    def test_resolution_layers_retain_unknowns(self):
        receipt = json.loads(Path("data/trust-resolution.json").read_text())
        counts = receipt["counts"]
        self.assertEqual(counts["semantic_declarations"], 2450)
        self.assertEqual(counts["module_resolved_declarations"], 2221)
        self.assertEqual(counts["unknown_declarations"], 229)
        self.assertEqual(counts["source_modules"], 468)
        self.assertEqual(counts["compiled_artifacts"], 413)
        self.assertEqual(len(receipt["mappings"]), 2450)
        self.assertEqual(receipt["trust_layers"]["root"], "not established")


if __name__ == "__main__":
    unittest.main()
