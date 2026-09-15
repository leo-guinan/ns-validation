# Experiment 03 — proof ↔ verifier alignment

This experiment compares the grounded mathematical proof graph with the separate Lean verification development without conflating their units.

Current objects:

- `G_proof_v1`: seven paper construction nodes and six literal interfaces.
- `G_verification`: 977 reachable Lean modules and 2,763 import edges.
- `G_declaration_source_scan`: ten declarations in the inspected theorem surface, with source-token references only.
- `interface-alignment.json`: explicit anchor mappings and unmapped/ambiguous results.

The source scan is not an elaborated dependency graph. It is a preflight inventory. The desired next artifact is a Lean-generated graph of constants referenced by elaborated declaration types and proof terms, followed by transitive cones and `#print axioms` receipts.

The falsifier is active: four of seven proof nodes currently have no source-supported Lean anchor, and three have only ambiguous name-based anchors. The graph was not modified to force agreement.

No formalization expansion, compression ratio, minimal interface, or ΔI is calculated.
