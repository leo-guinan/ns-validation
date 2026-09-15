"""Validate a literal proof-interface outline without inferring minimality."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_NODE_FIELDS = {"id", "name", "assumptions", "internal_construction", "exported_object", "validation_condition", "source_refs"}
REQUIRED_EDGE_FIELDS = {"from", "to", "literal_interface", "source_refs"}


def load_proof_graph(path: str | Path) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("nodes"), list) or not isinstance(payload.get("edges"), list):
        raise ValueError("proof graph must contain nodes and edges arrays")
    node_ids = set()
    for node in payload["nodes"]:
        if not isinstance(node, dict) or not REQUIRED_NODE_FIELDS <= node.keys():
            raise ValueError(f"node is missing required fields: {node}")
        if node["id"] in node_ids:
            raise ValueError(f"duplicate node id: {node['id']}")
        node_ids.add(node["id"])
    for edge in payload["edges"]:
        if not isinstance(edge, dict) or not REQUIRED_EDGE_FIELDS <= edge.keys():
            raise ValueError(f"edge is missing required fields: {edge}")
        if edge["from"] not in node_ids or edge["to"] not in node_ids:
            raise ValueError(f"edge refers to unknown node: {edge}")
    return payload


def graph_edges(graph: dict[str, Any]) -> list[tuple[str, str]]:
    return [(edge["from"], edge["to"]) for edge in graph["edges"]]


def render_proof_graph_report(graph: dict[str, Any]) -> str:
    lines = [
        "Experiment 02 — proof-interface graph",
        f"Status: {graph['status']}",
        f"Evidence boundary: {graph['evidence_boundary']}",
        "",
        "Nodes:",
    ]
    for node in graph["nodes"]:
        lines.extend([
            f"- {node['id']}: {node['name']}",
            f"  assumptions: {'; '.join(node['assumptions'])}",
            f"  exports: {node['exported_object']}",
            f"  validation: {node['validation_condition']}",
            f"  source refs: {', '.join(node['source_refs'])}",
        ])
    lines.append("\nLiteral interfaces:")
    for edge in graph["edges"]:
        lines.append(f"- {edge['from']} -> {edge['to']}: {edge['literal_interface']}")
    lines.extend(["", "Not yet measured:"])
    lines.extend(f"- {item}" for item in graph.get("not_yet_measured", []))
    return "\n".join(lines) + "\n"
