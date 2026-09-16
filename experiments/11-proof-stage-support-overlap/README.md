# Experiment 11 — proof-stage support overlap

Experiment 11 reconnects the human proof graph to elaborated Lean support without forcing a correspondence. Experiment 03 records four unmapped proof nodes and three ambiguous source anchors. Only the two `source_supported_anchor` declarations for `compact_forcing` are traversed.

```text
NavierStokesR3.theorem_1_1_with_initial_rest: 886 local / 2450 frontier
NavierStokesR3.theorem_1_1:                   888 local / 2450 frontier
```

At declaration resolution, support means bounded local declarations plus the external frontier. External support is then resolved through the Experiment 10 mapping:

```text
first anchor: 3336 declarations / 468 modules / 413 artifacts / 3 packages
second anchor:3338 declarations / 468 modules / 413 artifacts / 3 packages
```

Pairwise overlap:

```text
declaration: intersection 3336, union 3338, Jaccard 0.9994008388256441
module:      intersection 468,  union 468,  Jaccard 1.0
artifact:    intersection 413,  union 413,  Jaccard 1.0
package:     intersection 3,    union 3,    Jaccard 1.0
```

The module/artifact/package resolutions cover the external frontier only. Project-local source-module/artifact provenance is not inferred. The six unmapped or ambiguous proof nodes remain non-comparable, and the falsifier remains triggered. No overlap value implies optimality, sufficiency, or semantic equivalence of the paper and Lean structures.
