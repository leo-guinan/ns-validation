# Experiment 02 — grounded proof and verification graphs

Experiment 01 remains frozen. The earlier outline is preserved as `proof-interface-graph.json` (v0).

## G_proof_v1

`proof-interface-graph-v1.json` is grounded in the retrieved 166-page OpenAI paper. Nodes follow the paper's actual construction sections (§4–§10), with page, theorem, proposition, lemma, and equation references. Each edge records the literal data passed between sections. It does not claim minimal sufficiency, compression, or independent validity.

## G_verification

`verification-graph.json` is a separate import-closure graph rooted at `NavierStokes`. It was generated from the pinned Lean repository commit in `data/proof-sources.json` and currently contains repository source modules and import edges. It is not a theorem dependency graph and is not merged into `G_proof_v1`.

The repository's comparator target is `NavierStokes.Comparator.navier_stokes_breakdown_R3`, with permitted axioms `propext`, `Quot.sound`, and `Classical.choice`. Kernel-elaborated theorem dependencies, formal literal interfaces, and an interface comparison remain unmeasured.

Build the verification graph with:

```text
python3 scripts/build_verification_graph.py /path/to/NavierStokesAndEuler data/verification-graph.json
```

Source artifact receipt: `data/proof-sources.json`.
