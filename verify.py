import json
from pathlib import Path
import sys
from typing import Any

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
ledger: Any
if source.exists():
    ledger = parse_markdown(source)
    json_path = write_json(ledger, Path("data") / "ledger.json")
    print(f"source_replay=available path={source}")
else:
    json_path = Path("data") / "ledger.json"
    if not json_path.exists():
        raise SystemExit(f"raw source unavailable and derived ledger missing: {source}")
    ledger = json.loads(json_path.read_text(encoding="utf-8"))
    print(f"source_replay=unavailable raw_source={source} derived_ledger={json_path}")
report_path = Path("data") / "report.txt"
if source.exists():
    report_path.write_text(render_report(ledger), encoding="utf-8")
    print(f"source={ledger.source}")
    print(f"sha256={ledger.source_sha256}")
    print(f"claims={len(ledger.claims)} metrics={len(ledger.metrics)} questions={len(ledger.research_questions)} boundaries={len(ledger.boundaries)}")
else:
    print(f"derived_ledger_sha256={ledger['source_sha256']}")
    print(f"claims={len(ledger['claims'])} metrics={len(ledger['metrics'])} questions={len(ledger['research_questions'])} boundaries={len(ledger['boundaries'])}")
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
transfer = json.loads((Path("data") / "environment-transfer.json").read_text(encoding="utf-8"))
print(f"experiment06_status={transfer['status']} direct_dependencies={transfer['elaborated_direct_dependencies']['count']}")
bounded = json.loads((Path("data") / "bounded-cone.json").read_text(encoding="utf-8"))
print(f"experiment07_status={bounded['status']} local={bounded['counts']['local_cone']} frontier={bounded['counts']['frontier']}")
sweep = json.loads((Path("data") / "boundary-sweep.json").read_text(encoding="utf-8"))
print(f"experiment08_status={sweep['status']} boundaries={len(sweep['boundaries'])}")
frontier = json.loads((Path("data") / "frontier-anatomy.json").read_text(encoding="utf-8"))
print(f"experiment09_status={frontier['status']} edges={frontier['graph']['edges']} frontier={frontier['graph']['frontier_declarations']}")
resolution = json.loads((Path("data") / "trust-resolution.json").read_text(encoding="utf-8"))
print(f"experiment10_status={resolution['status']} modules={resolution['counts']['source_modules']} artifacts={resolution['counts']['compiled_artifacts']}")
overlap = json.loads((Path("data") / "proof-stage-overlap.json").read_text(encoding="utf-8"))
print(f"experiment11_status={overlap['status']} grounded={len(overlap['grounded_support'])}")
delta = json.loads((Path("data") / "marginal-theorem-delta.json").read_text(encoding="utf-8"))
print(f"experiment12_status={delta['status']} marginal={delta['marginal_support']['size']} subset={delta['support_accounting']['containment']}")
transitions = json.loads((Path("data") / "marginal-proof-transitions.json").read_text(encoding="utf-8"))
print(f"experiment13_status={transitions['status']} nodes={len(transitions['nodes'])} transitions={len(transitions['transitions'])}")
anatomy = json.loads((Path("data") / "transition-anatomy.json").read_text(encoding="utf-8"))
print(f"experiment14_status={anatomy['status']} unchanged={anatomy['distribution']['class_counts']['frontier_unchanged']} expanding={anatomy['distribution']['class_counts']['frontier_expanding']}")
capital = json.loads((Path("data") / "verification-capital-reuse.json").read_text(encoding="utf-8"))
print(f"experiment15_status={capital['status']} profiles={len(capital['frontier_expansion_profiles'])} dominators={sum(bool(x['dominates_selected_nodes']) for x in capital['domination']['edge_dominators'])}")
active = json.loads((Path("data") / "active-frontier-reuse.json").read_text(encoding="utf-8"))
print(f"experiment16_status={active['status']} observations={active['summary']['downstream_transition_observations']} direct_nonzero={active['summary']['D_nonzero_count']} transitive_nonzero={active['summary']['T_nonzero_count']}")
attribution = json.loads((Path("data") / "frontier-expansion-attribution.json").read_text(encoding="utf-8"))
print(f"experiment17_status={attribution['status']} expanding={attribution['summary']['expanding_edges']} fractions={attribution['summary']['active_at_entry_fraction']}")
entry = json.loads((Path("data") / "entry-interface-anatomy.json").read_text(encoding="utf-8"))
print(f"experiment18_status={entry['status']} graphs={len(entry['graphs'])} access_width={entry['summary']['access_width']}")
gateway = json.loads((Path("data") / "gateway-necessity.json").read_text(encoding="utf-8"))
print(f"experiment19_status={gateway['status']} lower={gateway['summary']['lower_bounds']} upper={gateway['summary']['greedy_upper_bounds']} exact={gateway['summary']['exact_values']}")
kernel = json.loads((Path("data") / "residual-gateway-kernel.json").read_text(encoding="utf-8"))
print(f"experiment20_status={kernel['status']} residual_frontier={kernel['summary']['residual_frontier_counts']} bounds={list(zip(kernel['summary']['total_lower_bounds'], kernel['summary']['total_upper_bounds']))}")
exact = json.loads((Path("data") / "exact-residual-components.json").read_text(encoding="utf-8"))
print(f"experiment21_status={exact['status']} totals={exact['summary']['exact_total_covers']} components={exact['summary']['component_counts']}")
backbone = json.loads((Path("data") / "optimal-interface-backbone.json").read_text(encoding="utf-8"))
print(f"experiment22_status={backbone['status']} totals={backbone['summary']['exact_total_covers']} optimal_counts={backbone['summary']['optimal_interface_counts']}")
identity = json.loads((Path("data") / "cross-transition-interface-identity.json").read_text(encoding="utf-8"))
print(f"experiment23_status={identity['status']} identical_2436={identity['summary']['three_2436_optima_identical']} contained={identity['summary']['any_2436_contained_in_2508']}")
edit = json.loads((Path("data") / "interface-edit-anatomy.json").read_text(encoding="utf-8"))
print(f"experiment24_status={edit['status']} removed={edit['comparison']['removed_count']} added={edit['comparison']['added_count']} small_subset_added={edit['small_interface_test']['small_subset_added']}")
flow = json.loads((Path("data") / "responsibility-flow-anatomy.json").read_text(encoding="utf-8"))
print(f"experiment25_status={flow['status']} shared={flow['frontier_sets']['shared_count']} new={flow['frontier_sets']['new_count']} weighted_edges={flow['edit']['nonzero_weight_edge_count']}")
embedding = json.loads((Path("data") / "subinterface-embedding-counterfactuals.json").read_text(encoding="utf-8"))
print(f"experiment26_status={embedding['status']} full_frontier_claims_withdrawn={embedding['scope_correction']['full_frontier_claims_withdrawn']}")
subset_lattice = json.loads((Path("data") / "a4-forbidden-subset-lattice.json").read_text(encoding="utf-8"))
print(f"experiment28_status={subset_lattice['status']} full_frontier_claims_withdrawn={subset_lattice['scope_correction']['full_frontier_claims_withdrawn']}")
memberwise = json.loads((Path("data") / "memberwise-feasibility-replacement.json").read_text(encoding="utf-8"))
print(f"experiment27_status={memberwise['status']} full_frontier_claims_withdrawn={memberwise['scope_correction']['full_frontier_claims_withdrawn']}")
rewiring = json.loads((Path("data") / "universal-310-cover-rewiring.json").read_text(encoding="utf-8"))
print(f"experiment29_status={rewiring['status']} full_frontier_claims_withdrawn={rewiring['scope_correction']['full_frontier_claims_withdrawn']}")
churn = json.loads((Path("data") / "minimum-churn-310-cover.json").read_text(encoding="utf-8"))
print(f"experiment30_status={churn['status']} full_frontier_claims_withdrawn={churn['scope_correction']['full_frontier_claims_withdrawn']}")
scope = json.loads((Path("data") / "frontier-scope-reconciliation.json").read_text(encoding="utf-8"))
print(f"experiment31_status={scope['status']} target={len(scope['frontiers']['target'])} delta_72={scope['delta_identity_checks']['delta_72_size']} delta_2508={scope['delta_identity_checks']['delta_2508_size']} contained={scope['delta_identity_checks']['delta_72_subset_delta_2508']}")
composition = json.loads((Path("data") / "full-target-composition-audit.json").read_text(encoding="utf-8"))
print(f"experiment32_status={composition['status']} target_width={composition['full_target_optimization']['minimum_cover_width']} union_width={composition['composition_overhead']['I2436_union_I72_size']} overhead={composition['composition_overhead']['I2436_union_I72_size'] - composition['full_target_optimization']['minimum_cover_width']}")