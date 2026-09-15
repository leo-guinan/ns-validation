#!/usr/bin/env python3
"""Extract the Lean import closure for the Navier–Stokes verification root."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

IMPORT = re.compile(r"^import\s+([A-Za-z0-9_.]+)\s*$", re.MULTILINE)


def module_path(root: Path, module: str) -> Path | None:
    candidate = root / (module.replace(".", "/") + ".lean")
    return candidate if candidate.exists() else None


def build(root: Path, entry: str) -> dict:
    queue = [entry]
    seen: set[str] = set()
    edges: list[dict[str, str]] = []
    nodes: dict[str, dict[str, str]] = {}
    while queue:
        module = queue.pop(0)
        if module in seen:
            continue
        seen.add(module)
        path = module_path(root, module)
        if path is None:
            nodes[module] = {"id": module, "kind": "external_or_generated"}
            continue
        nodes[module] = {"id": module, "kind": "lean_source", "path": str(path.relative_to(root))}
        for imported in IMPORT.findall(path.read_text(encoding="utf-8")):
            edges.append({"from": module, "to": imported, "kind": "import"})
            if imported not in seen:
                queue.append(imported)
    return {
        "experiment": "02-proof-interface-graph",
        "graph": "G_verification",
        "status": "repository_import_closure",
        "source": {
            "repository": "https://github.com/openai/NavierStokesAndEuler",
            "commit": "f9e8bc5b38b6e212696e8a30e3e91517af887bbd",
            "entry_module": entry,
            "comparator_target": "NavierStokes.Comparator.navier_stokes_breakdown_R3",
            "permitted_axioms": ["propext", "Quot.sound", "Classical.choice"],
        },
        "nodes": list(nodes.values()),
        "edges": edges,
        "not_yet_measured": [
            "kernel dependency graph after elaboration",
            "theorem-to-theorem dependency graph",
            "formal literal interfaces",
            "interface delta versus G_proof_v1",
            "build receipt in this environment",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--entry", default="NavierStokes")
    args = parser.parse_args()
    args.output.write_text(json.dumps(build(args.root, args.entry), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
