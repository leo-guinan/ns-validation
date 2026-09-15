#!/usr/bin/env python3
"""Resolve frontier declarations through .ilean module metadata and package pins."""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

def git_head(path: Path) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return None

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("root",type=Path); ap.add_argument("input",type=Path); ap.add_argument("output",type=Path); args=ap.parse_args()
    root=args.root; source=json.loads(args.input.read_text())
    frontier=sorted({b for _,b in source["edges"]})
    records={n:{"declaration":n,"source_modules":set(),"ilean_files":set()} for n in frontier}
    for p in root.glob(".lake/**/*.ilean"):
        try: obj=json.loads(p.read_text())
        except Exception: continue
        module=obj.get("module")
        for key in obj.get("references",{}):
            try: ref=json.loads(key)
            except Exception: continue
            c=ref.get("c",{}); short=c.get("n"); full_candidates={short}
            if module and short: full_candidates.add(f"{module}.{short}")
            for candidate in full_candidates:
                if candidate in records:
                    records[candidate]["source_modules"].add(c.get("m") or "unknown")
                    records[candidate]["ilean_files"].add(str(p.relative_to(root)))
    package_heads={
      "mathlib":{"package":"mathlib","commit":git_head(root/".lake/packages/mathlib")},
      "Comparator":{"package":"Comparator","commit":git_head(root/".lake/packages/Comparator")},
    }
    toolchain=Path.home()/".elan/toolchains/leanprover--lean4---v4.34.0-rc2"
    mappings=[]
    for n,r in records.items():
        mods=sorted(r["source_modules"]); files=sorted(r["ilean_files"])
        packages=set(); artifacts=set(); source_files=set()
        for m in mods:
            if m.startswith("Mathlib"):
                packages.add("mathlib")
                sf=root/".lake/packages/mathlib"/(m.replace(".","/")+".lean")
                if sf.exists(): source_files.add(str(sf.relative_to(root)))
                af=root/".lake/packages/mathlib/.lake/build/lib/lean"/(m.replace(".","/")+".olean")
                if af.exists(): artifacts.add(str(af.relative_to(root/".lake/packages/mathlib")))
            elif m.startswith("Comparator"):
                packages.add("Comparator")
            elif m.startswith(("Init","Lean","Batteries")):
                packages.add("lean-toolchain")
            elif m: packages.add("unknown")
        mappings.append({"declaration":n,"source_modules":mods,"source_files":sorted(source_files),"compiled_artifacts":sorted(artifacts),"packages":sorted(packages),"ilean_evidence_file_count":len(files),"ilean_evidence_samples":files[:3],"provenance_status":"resolved_module" if mods else "unknown"})
    resolved=[x for x in mappings if x["source_modules"]]
    out={"experiment":"10-trust-resolution-stack","status":"declaration_provenance_resolved_with_unknowns","source_commit":"f9e8bc5b38b6e212696e8a30e3e91517af887bbd","target":source["target"],"input_frontier_declarations":len(frontier),"resolution_policy":"Use .ilean reference records; retain all module candidates; never infer module from namespace alone.","package_pins":package_heads,"counts":{"semantic_declarations":len(frontier),"module_resolved_declarations":len(resolved),"unknown_declarations":len(frontier)-len(resolved),"source_modules":len({m for x in mappings for m in x["source_modules"]}),"source_files":len({f for x in mappings for f in x["source_files"]}),"compiled_artifacts":len({a for x in mappings for a in x["compiled_artifacts"]}),"packages":len({p for x in mappings for p in x["packages"]})},"trust_layers":{"semantic":"frontier declaration identities","source_module":".ilean module field","compiled_artifact":"path exists only when located","package":"package classification plus pinned checkout commit","root":"not established"},"mappings":mappings,"not_yet_measured":["independent artifact signatures","artifact provenance beyond local cache","root trust assumptions","minimal operational interface"]}
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out["counts"]))
if __name__=="__main__": main()
