import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from ns_validation import (
    build_lifecycle_ledger,
    graph_edges,
    load_stages,
    load_proof_graph,
    parse_markdown,
    render_lifecycle_report,
    render_proof_graph_report,
    render_report,
    stage_edges,
    write_json,
    write_lifecycle_ledger,
)

source = Path.home() / "Downloads" / "NS Validation idea.md"
if not source.exists():
    raise SystemExit(f"required source not found: {source}")
ledger = parse_markdown(source)
json_path = write_json(ledger, Path("data") / "ledger.json")
report_path = Path("data") / "report.txt"
report_path.write_text(render_report(ledger), encoding="utf-8")
print(f"source={ledger.source}")
print(f"sha256={ledger.source_sha256}")
print(f"claims={len(ledger.claims)} metrics={len(ledger.metrics)} questions={len(ledger.research_questions)} boundaries={len(ledger.boundaries)}")
print(f"json={json_path} bytes={json_path.stat().st_size}")
print(f"report={report_path.resolve()} bytes={report_path.stat().st_size}")
stages = load_stages(Path("data") / "proof-stages.json")
print(f"stages={len(stages)} edges={len(stage_edges(stages))}")
lifecycle = write_lifecycle_ledger(
    Path("data") / "proof-stages.json",
    Path("data") / "source-ledger.json",
    Path("data") / "experiment01-ledger.json",
)
lifecycle_report = Path("data") / "experiment01-report.txt"
lifecycle_report.write_text(render_lifecycle_report(build_lifecycle_ledger(Path("data") / "proof-stages.json", Path("data") / "source-ledger.json")), encoding="utf-8")
print(f"experiment01_ledger={lifecycle} bytes={lifecycle.stat().st_size}")
print(f"experiment01_report={lifecycle_report.resolve()} bytes={lifecycle_report.stat().st_size}")
proof_graph = load_proof_graph(Path("data") / "proof-interface-graph.json")
proof_report = Path("data") / "experiment02-outline-report.txt"
proof_report.write_text(render_proof_graph_report(proof_graph), encoding="utf-8")
print(f"experiment02_nodes={len(proof_graph['nodes'])} edges={len(graph_edges(proof_graph))}")
print(f"experiment02_report={proof_report.resolve()} bytes={proof_report.stat().st_size}")
proof_graph_v1 = load_proof_graph(Path("data") / "proof-interface-graph-v1.json")
verification_graph = json.loads((Path("data") / "verification-graph.json").read_text(encoding="utf-8"))
print(f"experiment02_v1_nodes={len(proof_graph_v1['nodes'])} edges={len(graph_edges(proof_graph_v1))}")
print(f"verification_nodes={len(verification_graph['nodes'])} edges={len(verification_graph['edges'])}")
alignment = json.loads((Path("data") / "interface-alignment.json").read_text(encoding="utf-8"))
scan = json.loads((Path("data") / "declaration-source-scan.json").read_text(encoding="utf-8"))
print(f"experiment03_status={alignment['status']} source_declarations={len(scan['nodes'])}")
print(f"experiment03_falsifier={alignment['falsifier']['result']}")
cone = json.loads((Path("data") / "elaborated-cone.json").read_text(encoding="utf-8"))
print(f"experiment04_status={cone['status']} target={cone['target']}")