# Experiment 15 — verification capital reuse

Experiment 15 analyzes the six frontier-expanding transitions in the selected six-node graph from Experiment 13.

For each edge it records the exact newly introduced frontier set `N`, the fraction retained in every reachable downstream selected node, and exact per-declaration downstream reuse counts.

Observed bounded profiles:

```text
72-declaration expansions:    all 72 identities persist to the reachable dissipation node
2436-declaration expansions:  all identities persist to 1, 2, or 4 reachable selected nodes
2508-declaration expansion:   all 2508 identities persist to its reachable node
```

A selected-graph dominator pass found two roots and zero dominating edges. Alternate paths prevent a chokepoint claim at this scope.

This measures persistence and reuse participation, not savings, causality, runtime cost, minimality, or optimality. The graph is selected and incomplete.
