# Experiment 56 — exact witness-network robustness

Optimality-blocking and feasibility-blocking are measured separately:

```text
τ: minimum deletions eliminating every current minimum-width cover
κ: minimum deletions making any cover infeasible
```

Pure substitution:

```text
120 components
τ = κ for all 120
```

Kernel results:

```text
component 8:  τ=4,  κ=4,  degraded width=4
component 11: τ=16, κ=21, degraded width=4
component 12: τ=1,  κ=2, degraded width=2
component 21: τ=1, κ=4, degraded width=3
component 45: τ=1, κ=2, degraded width=2
```

The four residual-backbone single deletions remain feasible but increase component minimum width. Singleton-private forced-world deletion is globally infeasible; optional and never-optimal single deletions preserve global minimum width.

The unconditioned full-system thresholds are `τ_full=1` and `κ_full=1`, because any one of the 58 singleton-private forced worlds makes the full cover infeasible. `degraded width` means the minimum surviving width for a preserved τ-sized optimality-blocking deletion witness that remains feasible; τ=κ does not imply every τ-sized deletion is infeasible.

These are combinatorial deletion tolerances, not operational reliability or semantic necessity.
