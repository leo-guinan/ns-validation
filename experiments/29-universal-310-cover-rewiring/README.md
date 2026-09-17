# Experiment 29 — universal 310-cover rewiring

The all-`A4`-forbidden witness `J310` is a valid 310-member cover. Compared with the unique 309-member optimum:

```text
309 optimum → 310 witness
intersection: 272
removed:     37
added:       38
symmetric difference: 75
```

All four `A4` declarations are removed, and the entire rigid `I72` block remains present in `J310`.

This measured +1-width witness is broadly rewired: it is not a four-for-four substitution. Its Jaccard overlap with the unique optimum is 272/347 ≈ 0.784, and 1,373/1,406 possible removed↔added responsibility pairs have nonzero literal overlap (≈97.65%). Because width-310 enumeration is not measured, these properties belong to this witness and are not claimed for every 310-member cover.

This remains a fixed set-cover result, not semantic replacement or causal transfer.
