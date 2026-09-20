import json
import unittest
from pathlib import Path


class ViolationBasisStateDecoderTests(unittest.TestCase):
    def test_basis_and_decoders(self):
        r = json.loads(Path("data/violation-basis-state-decoder.json").read_text())
        self.assertEqual(r["status"], "exact_violation_basis_and_state_decoder_measured")
        self.assertEqual([(x["component_index"], x["evaluation_matrix_rank"], x["violation_predicates_basis_of_zero_origin_space"], x["repair_bit_decoders_verified"], x["onehot_decoders_verified"]) for x in r["components"]], [(8, 3, True, True, True), (11, 15, True, True, True)])
        for x in r["components"]:
            a = x["evaluation_matrix"]
            ai = x["evaluation_matrix_inverse"]
            self.assertEqual([[sum(a[i][k] * ai[k][j] for k in range(len(a))) % 2 for j in range(len(a))] for i in range(len(a))], [[int(i == j) for j in range(len(a))] for i in range(len(a))])
            self.assertEqual([[sum(ai[i][k] * a[k][j] for k in range(len(a))) % 2 for j in range(len(a))] for i in range(len(a))], [[int(i == j) for j in range(len(a))] for i in range(len(a))])


if __name__ == "__main__":
    unittest.main()
