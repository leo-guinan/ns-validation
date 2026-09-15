#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ns_validation.alignment import write_source_scan

parser = argparse.ArgumentParser()
parser.add_argument("root", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("files", nargs="*", default=[
    "NavierStokes/R3/Theorem.lean",
    "NavierStokes/ComparatorTheorem.lean",
    "NavierStokes/ComparatorSolution.lean",
])
args = parser.parse_args()
write_source_scan(args.root, args.output, args.files)
print(args.output)
