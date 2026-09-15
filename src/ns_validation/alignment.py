"""Declaration-level alignment helpers for Experiment 03.

The checked-in receipt deliberately distinguishes source declaration scans from
Lean elaboration. Use `build_source_scan` only as a pre-elaboration inventory;
it must not be reported as a kernel dependency graph.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

DECL = re.compile(r"^\s*(theorem|lemma|def|abbrev|opaque|structure|class)\s+([A-Za-z0-9_']+)", re.MULTILINE)
IMPORT = re.compile(r"^import\s+([A-Za-z0-9_.]+)\s*$", re.MULTILINE)


def source_declarations(path: Path, namespace: str = "") -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    matches = list(DECL.finditer(text))
    result = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.start():end]
        line = text.count("\n", 0, match.start()) + 1
        name = f"{namespace}.{match.group(2)}" if namespace else match.group(2)
        result.append({"name": name, "kind": match.group(1), "file": str(path), "line": line, "body": body})
    return result


def build_source_scan(root: Path, files: list[str]) -> dict[str, Any]:
    declarations: list[dict[str, Any]] = []
    for relative in files:
        path = root / relative
        declarations.extend([{**d, "file": relative} for d in source_declarations(path)])
    names = {d["name"].split(".")[-1]: d["name"] for d in declarations}
    nodes = []
    for declaration in declarations:
        refs = sorted({names[token] for token in re.findall(r"\b[A-Za-z_][A-Za-z0-9_']*\b", declaration["body"]) if token in names and names[token] != declaration["name"]})
        nodes.append({k: declaration[k] for k in ("name", "kind", "file", "line")} | {"source_token_dependencies": refs})
    return {
        "experiment": "03-proof-verifier-alignment",
        "graph": "G_declaration_source_scan",
        "status": "syntax_inventory_not_elaborated",
        "source_files": files,
        "nodes": nodes,
        "edges": [{"from": n["name"], "to": dep, "kind": "source_token_reference"} for n in nodes for dep in n["source_token_dependencies"]],
        "not_yet_measured": ["elaborated declaration dependencies", "proof-term dependencies", "kernel axiom receipt"],
    }


def write_source_scan(root: str | Path, output: str | Path, files: list[str]) -> Path:
    result = build_source_scan(Path(root), files)
    path = Path(output)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return path
