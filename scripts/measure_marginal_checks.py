#!/usr/bin/env python3
"""Measure warm module and theorem-interface checks without claiming theorem-isolated cost."""
from __future__ import annotations
import json, subprocess, time
import argparse
from pathlib import Path

def lake_size(root: Path) -> int:
    return sum(p.stat().st_size for p in (root/".lake").rglob("*") if p.is_file())

def run(root: Path, label: str, command: list[str]) -> dict:
    before=lake_size(root); start=time.monotonic()
    proc=subprocess.run(command, cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"label":label,"seconds":round(time.monotonic()-start,3),"bytes_changed":lake_size(root)-before,"exit_code":proc.returncode}

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("lean_root",type=Path); args=ap.parse_args(); root=args.lean_root.resolve()
    checks=[run(root,"module_recheck",["lake","build","NavierStokes.R3.Theorem"]),run(root,"initial_rest_interface_check",["lake","env","lean",str(Path(__file__).resolve().parent/"check_initial_rest.lean")]),run(root,"final_theorem_interface_check",["lake","env","lean",str(Path(__file__).resolve().parent/"check_final_theorem.lean")])]
    print(json.dumps({"environment":"cached","lean_root":str(root),"checks":checks,"target_olean_present":(root/".lake/build/lib/lean/NavierStokes/R3/Theorem.olean").exists()}))
if __name__=="__main__": main()
