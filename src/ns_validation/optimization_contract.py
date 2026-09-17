"""Canonical fingerprints for optimization contracts."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def sha256_canonical(value: Any) -> str:
    """Hash JSON-compatible data with stable ordering and separators."""
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()


def contract_fingerprint(
    locals_set: Any,
    frontier_set: Any,
    edges: Any,
    objective: Any,
    constraints: Any,
) -> dict[str, str]:
    """Return component hashes and a combined optimization-contract hash."""
    components = {
        "h_L": sha256_canonical(locals_set),
        "h_F": sha256_canonical(frontier_set),
        "h_E": sha256_canonical(edges),
        "h_O": sha256_canonical(objective),
        "h_K": sha256_canonical(constraints),
    }
    joined = "".join(components[key] for key in ("h_L", "h_F", "h_E", "h_O", "h_K"))
    return {**components, "H_contract": hashlib.sha256(joined.encode()).hexdigest()}
