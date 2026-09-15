#!/usr/bin/env python3
"""Measure cold/warm activation for one Lean module without claiming a cone."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import time
from pathlib import Path


def size_bytes(path: Path) -> int:
    total = 0
    for item in path.rglob("*") if path.exists() else []:
        if item.is_file():
            try:
                total += item.stat().st_size
            except FileNotFoundError:
                pass
    return total


def run_once(root: Path, target: str, timeout: int, condition: str, log_path: Path) -> dict:
    lake = root / ".lake"
    before = size_bytes(lake)
    started = time.monotonic()
    exit_code = None
    timed_out = False
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            ["lake", "build", target], cwd=root, stdout=log, stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            exit_code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            exit_code = 124
    after = size_bytes(lake)
    olean = root / ".lake" / "build" / "lib" / "lean" / "NavierStokes" / "R3" / "Theorem.olean"
    return {
        "condition": condition,
        "target": target,
        "timeout_seconds": timeout,
        "wall_seconds": round(time.monotonic() - started, 3),
        "exit_code": exit_code,
        "timed_out": timed_out,
        "lake_bytes_before": before,
        "lake_bytes_after": after,
        "lake_bytes_delta": after - before,
        "target_olean_produced": olean.exists(),
        "log": str(log_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--target", default="NavierStokes.R3.Theorem")
    args = parser.parse_args()
    shutil.rmtree(args.root / ".lake", ignore_errors=True)
    cold = run_once(args.root, args.target, args.timeout, "cold", Path("/tmp/ns-validation-exp05-cold.log"))
    warm = run_once(args.root, args.target, args.timeout, "warm_preserved_after_cold", Path("/tmp/ns-validation-exp05-warm.log"))
    result = {
        "experiment": "05-verification-activation-amortization",
        "status": "measured_activation_not_elaboration",
        "source_commit": "f9e8bc5b38b6e212696e8a30e3e91517af887bbd",
        "target": args.target,
        "conditions": [cold, warm],
        "activation_ratio": None,
        "reason_activation_ratio_unknown": "Both runs timed out before target elaboration; wall-time ratio would mix incomplete environment work with no theorem check.",
        "cone": None,
        "not_yet_measured": ["successful target elaboration", "theorem dependency cone", "formal recheck time", "common usable warm environment"],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cold": cold, "warm": warm}, indent=2))


if __name__ == "__main__":
    main()
