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
exchange = json.loads((Path("data") / "full-target-optimum-exchange.json").read_text(encoding="utf-8"))
print(f"experiment33_status={exchange['status']} feasible_forbidden={exchange['member_sweep']['feasible_count']} unresolved_forbidden={exchange['member_sweep']['infeasible_or_timeout_count']} composition_symdiff={exchange['composition_anatomy']['symmetric_difference_size']}")
historical = json.loads((Path("data") / "historical-delta-contract-replay.json").read_text(encoding="utf-8"))
print(f"experiment34_status={historical['status']} nodes={historical['replay_observation']['nodes_emitted']}/{historical['replay_observation']['nodes_requested']} contract_hash={historical['contract_components']['H_contract']}")
surgical = json.loads((Path("data") / "surgical-historical-contract-replay.json").read_text(encoding="utf-8"))
print(f"experiment35_status={surgical['status']} target_frontier={surgical['node_reproduction']['target']['frontier_count']} delta={surgical['delta_reconstruction']['frontier_size']} optimization_contract={surgical['optimization_contract']['status']}")
archaeology = json.loads((Path("data") / "historical-candidate-reduction-archaeology.json").read_text(encoding="utf-8"))
print(f"experiment36_status={archaeology['status']} raw_locals={archaeology['raw_input']['count']} exact_882={archaeology['archaeology_search']['preserved_exact_882_identity_list']} exact_741={archaeology['archaeology_search']['preserved_exact_741_identity_list']}")
scope = json.loads((Path("data") / "scope-effect-under-fixed-contract.json").read_text(encoding="utf-8"))
print(f"experiment37_status={scope['status']} full_width={scope['contracts']['full']['minimum_cover_width']} delta_width={scope['contracts']['delta_B_to_T']['minimum_cover_width']} I_delta={scope['known_optima_probe']['I2508']['delta_coverage']} J_delta={scope['known_optima_probe']['J_full']['delta_coverage']}")
face = json.loads((Path("data") / "optimal-face-scope-redundancy.json").read_text(encoding="utf-8"))
print(f"experiment38_status={face['status']} inherited={face['inherited_frontier_count']} feasible_noncoverage={face['summary']['feasible_noncoverage_count']} proven_infeasible={face['summary']['proven_infeasible_count']} timeouts={face['summary']['timeout_count']}")
activation = json.loads((Path("data") / "scope-activation-depth.json").read_text(encoding="utf-8"))
print(f"experiment39_status={activation['status']} optimal={activation['summary']['optimal_count']} infeasible={activation['summary']['infeasible_count']} timeouts={activation['summary']['timeout_or_other_count']} scope_gap={activation['summary']['scope_activation_gap']}")
subsumption = json.loads((Path("data") / "constraint-subsumption-analysis.json").read_text(encoding="utf-8"))
print(f"experiment40_status={subsumption['status']} frontier={subsumption['counts']['frontier_identities']} unique_neighborhoods={subsumption['counts']['unique_neighborhoods']} basis={subsumption['counts']['inclusion_minimal_basis_classes']} removed={subsumption['counts']['constraints_removed_by_basis']}")
components = json.loads((Path("data") / "basis-incidence-components.json").read_text(encoding="utf-8"))
print(f"experiment41_status={components['status']} components={components['summary']['component_count']} width={components['summary']['minimum_width_sum']} slack={components['summary']['slack_sum']} optima={components['summary']['global_optimum_count']} backbone={components['summary']['global_backbone_count']}")
shell = json.loads((Path("data") / "exact-flexible-shell.json").read_text(encoding="utf-8"))
print(f"experiment42_status={shell['status']} candidates={shell['candidate_universe']['total']} support={shell['optimum_support']['support_size']} shell={shell['optimum_support']['flexible_shell_size']} backbone={shell['optimum_support']['backbone_size']}")
participation = json.loads((Path("data") / "exact-participation-spectrum.json").read_text(encoding="utf-8"))
print(f"experiment43_status={participation['status']} backbone={participation['candidate_classes']['backbone']} optional={participation['candidate_classes']['optional_optimal']} shell_sum={participation['checksum']['optional_shell_sum']} p_min={participation['spectrum']['optional_fraction_min']} p_max={participation['spectrum']['optional_fraction_max']}")
exchange = json.loads((Path("data") / "optimum-exchange-geometry.json").read_text(encoding="utf-8"))
print(f"experiment44_status={exchange['status']} components={exchange['summary']['component_count']} connected={exchange['summary']['global_exchange_graph_connected']} diameter={exchange['summary']['global_diameter']} edges={exchange['summary']['total_local_exchange_edges']}")
geodesic = json.loads((Path("data") / "geodesic-exchange-and-basis-axiom.json").read_text(encoding="utf-8"))
print(f"experiment45_status={geodesic['status']} geodesic={geodesic['summary']['all_components_geodesic']} detour={geodesic['summary']['maximum_detour']} diameter={geodesic['summary']['global_diameter']} matroid={geodesic['summary']['all_components_satisfy_basis_exchange_axiom']}")
precedence = json.loads((Path("data") / "exchange-precedence.json").read_text(encoding="utf-8"))
print(f"experiment46_status={precedence['status']} pairs={precedence['summary']['ordered_pair_count']} precedence_pairs={precedence['summary']['pairs_with_precedence']} max_depth={precedence['summary']['maximum_precedence_depth']}")
retention = json.loads((Path("data") / "geodesic-retention-and-poset-test.json").read_text(encoding="utf-8"))
print(f"experiment47_status={retention['status']} pairs={retention['summary']['ordered_pair_count']} full_retention={retention['summary']['full_retention_pairs']} partial={retention['summary']['partial_retention_pairs']} convex={retention['summary']['geodesically_convex']} poset_failures={retention['summary']['pairs_not_poset_exact']}")
continuation = json.loads((Path("data") / "continuation-state-sufficiency.json").read_text(encoding="utf-8"))
print(f"experiment48_status={continuation['status']} pairs={continuation['summary']['ordered_pair_count']} depth_collisions={continuation['summary']['pairs_with_depth_collision']} removal_collisions={continuation['summary']['pairs_with_removal_collision']} addition_collisions={continuation['summary']['pairs_with_addition_collision']}")
distinguishing = json.loads((Path("data") / "minimum-distinguishing-coordinates.json").read_text(encoding="utf-8"))
print(f"experiment49_status={distinguishing['status']} raw_pairs={distinguishing['audit']['raw_state_pair_count']} removal_dimension={distinguishing['removal']['minimum_dimension']} addition_dimension={distinguishing['addition']['minimum_dimension']} singleton_certified={distinguishing['removal']['all_coordinates_singleton_certified'] and distinguishing['addition']['all_coordinates_singleton_certified']}")
local_dimensions = json.loads((Path("data") / "pair-local-state-dimensions.json").read_text(encoding="utf-8"))
print(f"experiment50_status={local_dimensions['status']} pairs={local_dimensions['summary']['ordered_pair_count']} max_m_R={local_dimensions['summary']['max_m_R']} max_m_A={local_dimensions['summary']['max_m_A']} equal_pairs={local_dimensions['summary']['pairs_m_R_equals_m_A']}")
atlas = json.loads((Path("data") / "dimensionality-atlas.json").read_text(encoding="utf-8"))
print(f"experiment51_status={atlas['status']} pairs={atlas['summary']['ordered_pair_count']} removal_cover={atlas['removal_world_cover']['minimum_world_count']} addition_cover={atlas['addition_world_cover']['minimum_world_count']} reversal_equal={atlas['summary']['reversal_family_mismatch_count'] == 0}")
decomposition = json.loads((Path("data") / "cover-gap-incidence-decomposition.json").read_text(encoding="utf-8"))
print(f"experiment52_status={decomposition['status']} global_dimensions={decomposition['unit_separation']['global_literal_vocabulary_dimensions']} removal_forced={decomposition['removal']['forced_world_count']} removal_residual={decomposition['removal']['residual_world_cover_count']} addition_forced={decomposition['addition']['forced_world_count']} addition_residual={decomposition['addition']['residual_world_cover_count']} singleton_forced={decomposition['removal']['all_forced_world_backbones_singleton'] and decomposition['addition']['all_forced_world_backbones_singleton']}")
components = json.loads((Path("data") / "residual-incidence-components.json").read_text(encoding="utf-8"))
print(f"experiment53_status={components['status']} removal_components={components['summary']['removal_component_count']} residual_dimensions={components['summary']['removal_coordinate_sum']} residual_width={components['summary']['removal_width_sum']} all_enumerated={components['summary']['removal_all_enumerated'] and components['summary']['addition_all_enumerated']}")
choice = json.loads((Path("data") / "cover-choice-classification.json").read_text(encoding="utf-8"))
print(f"experiment54_status={choice['status']} components={choice['summary']['component_count']} kernel={choice['summary']['kernel_component_count']} saving={choice['summary']['kernel_saving_sum']} residual_partition={choice['derived_classification']['residual_backbone_count']}+{choice['derived_classification']['residual_optional_optimal_count']}+{choice['derived_classification']['residual_never_optimal_count']} reversal_verified={choice['summary']['reversal_component_correspondence_verified']}")
participation = json.loads((Path("data") / "exact-witness-participation.json").read_text(encoding="utf-8"))
print(f"experiment55_status={participation['status']} worlds={participation['summary']['world_count']} backbone_mass={participation['summary']['backbone_participation']} optional_mass={participation['summary']['optional_participation']} optional_range={participation['summary']['optional_min']}..{participation['summary']['optional_max']}")