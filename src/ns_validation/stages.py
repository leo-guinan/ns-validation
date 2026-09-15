"""Explicit stage and evidence models for the validation-architecture study."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_STAGE_FIELDS = {
    "id",
    "name",
    "predecessors",
    "work",
    "state_exported",
    "verification_burden",
    "trust_assumptions",
}


@dataclass(frozen=True)
class Stage:
    id: str
    name: str
    predecessors: list[str]
    work: str
    state_exported: str
    verification_burden: str
    trust_assumptions: list[str]
    evidence_ids: list[str]


def load_stages(path: str | Path) -> list[Stage]:
    """Load and structurally validate a stage model; no scientific claims are inferred."""
    payload: Any = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("stage model must be a JSON array")
    stages: list[Stage] = []
    ids: set[str] = set()
    for item in payload:
        if not isinstance(item, dict) or not REQUIRED_STAGE_FIELDS <= item.keys():
            raise ValueError(f"stage is missing required fields: {item}")
        stage = Stage(
            id=item["id"],
            name=item["name"],
            predecessors=item["predecessors"],
            work=item["work"],
            state_exported=item["state_exported"],
            verification_burden=item["verification_burden"],
            trust_assumptions=item["trust_assumptions"],
            evidence_ids=item.get("evidence_ids", []),
        )
        if stage.id in ids:
            raise ValueError(f"duplicate stage id: {stage.id}")
        ids.add(stage.id)
        stages.append(stage)
    for stage in stages:
        unknown = set(stage.predecessors) - ids
        if unknown:
            raise ValueError(f"{stage.id} refers to unknown predecessor(s): {sorted(unknown)}")
    return stages


def stage_edges(stages: list[Stage]) -> list[tuple[str, str]]:
    """Return directed predecessor -> stage edges in stable order."""
    return [(predecessor, stage.id) for stage in stages for predecessor in stage.predecessors]
