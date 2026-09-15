"""Build the Experiment 01 lifecycle ledger without inventing missing measurements."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _read(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _evidence_by_id(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {record["id"]: record for record in records}


def _evidence_refs(ids: list[str], evidence: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": evidence[item]["id"],
            "provenance": evidence[item]["provenance"],
            "status": evidence[item]["status"],
            "source": evidence[item]["source"],
        }
        for item in ids
    ]


def build_lifecycle_ledger(stages_path: str | Path, evidence_path: str | Path) -> dict[str, Any]:
    stages = _read(stages_path)
    evidence = _evidence_by_id(_read(evidence_path))
    records: list[dict[str, Any]] = []
    for stage in stages:
        refs = _evidence_refs(stage.get("evidence_ids", []), evidence)
        records.append(
            {
                "stage_id": stage["id"],
                "stage": stage["name"],
                "work": {
                    "construction": {"value": None, "unit": None, "status": "unknown"},
                    "validation": {"value": None, "unit": None, "status": "unknown"},
                    "replay": {"value": None, "unit": None, "status": "unknown"},
                    "observations": _work_observations(stage["id"], evidence),
                },
                "exported_state": {
                    "description": stage["state_exported"],
                    "size": {"value": None, "unit": None, "status": "unknown"},
                },
                "next_stage": _next_stage(stage["id"], stages),
                "downstream_verification_burden": stage["verification_burden"],
                "trust_assumptions": stage["trust_assumptions"],
                "provenance_quality": _provenance_quality(refs),
                "evidence_refs": refs,
                "edgewise_compression_ratio": {
                    "value": None,
                    "status": "unsupported_missing_state_and_interface_sizes",
                    "size_unit": None,
                },
            }
        )
    return {
        "experiment": "01-cost-ledger",
        "status": "prospective",
        "research_question": "How does an expensive mathematical search become a progressively cheaper, more durable object of trust?",
        "metric_policy": "Native-unit observations only; unknown quantities remain null; no cross-unit ratios are inferred.",
        "stages": records,
        "supported_metrics": {
            "reported_search_hours": 88,
            "reported_search_messages": 2700000,
            "reported_search_output_tokens": 130000000000,
            "reported_formalization_hours": 17,
            "reported_proof_pages": 166,
        },
        "unsupported_metrics": [
            "verification_compression_ratio",
            "edgewise_interface_compression_ratio",
            "verification_cost",
            "replay_cost",
            "exported_state_bytes",
            "interface_bytes",
            "verification_break_even",
        ],
    }


def _work_observations(stage_id: str, evidence: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    mapping = {
        "search": ["e-search-scale"],
        "proof-construction": ["e-proof-length"],
        "formalization": ["e-formalization-time"],
    }
    observations = []
    for evidence_id in mapping.get(stage_id, []):
        record = evidence[evidence_id]
        value = record.get("value")
        if isinstance(value, dict):
            for key, item in value.items():
                observations.append({"measure": key, "value": item, "provenance": record["provenance"], "unit": record["unit"], "source": record["source"]})
        else:
            observations.append({"measure": "reported_quantity", "value": value, "provenance": record["provenance"], "unit": record["unit"], "source": record["source"]})
    return observations


def _next_stage(stage_id: str, stages: list[dict[str, Any]]) -> str | None:
    for stage in stages:
        if stage_id in stage.get("predecessors", []):
            return stage["id"]
    return None


def _provenance_quality(refs: list[dict[str, Any]]) -> str:
    if not refs:
        return "unavailable"
    if all(item["status"] == "independently_verified" for item in refs):
        return "independently_verified"
    if all(item["status"] == "locally_checked" for item in refs):
        return "locally_checked"
    return "source-reported_unverified"


def write_lifecycle_ledger(stages_path: str | Path, evidence_path: str | Path, output: str | Path) -> Path:
    destination = Path(output).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_lifecycle_ledger(stages_path, evidence_path), indent=2) + "\n", encoding="utf-8")
    return destination


def render_lifecycle_report(ledger: dict[str, Any]) -> str:
    lines = [
        "Experiment 01 — lifecycle cost/state ledger",
        f"Status: {ledger['status']}",
        ledger["metric_policy"],
        "",
    ]
    for record in ledger["stages"]:
        lines.extend([
            record["stage"],
            f"  provenance quality: {record['provenance_quality']}",
            f"  exported state: {record['exported_state']['description']}",
            f"  exported-state size: {record['exported_state']['size']['status']}",
            f"  next stage: {record['next_stage'] or 'none'}",
            f"  verification burden: {record['downstream_verification_burden']}",
            f"  edgewise compression: {record['edgewise_compression_ratio']['status']}",
            f"  observations: {len(record['work']['observations'])}",
        ])
        for observation in record["work"]["observations"]:
            lines.append(f"    - {observation['measure']}={observation['value']} {observation['unit']} ({observation['provenance']})")
        lines.append("")
    lines.append("Supported numeric metrics:")
    lines.extend(f"  {key}: {value}" for key, value in ledger["supported_metrics"].items())
    lines.append("Unsupported metrics remain explicitly listed in the JSON ledger.")
    return "\n".join(lines) + "\n"
