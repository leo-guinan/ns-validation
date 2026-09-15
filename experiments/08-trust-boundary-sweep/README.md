# Experiment 08 — trust-boundary sweep

Target: `NavierStokesR3.coreBreakdownStatement`.

The same elaborated target was traversed under three explicit expansion policies:

```text
B0: target only
B1: NavierStokesR3 declarations through depth 1
B2: all NavierStokesR3 declarations
```

Observed boundary curve:

```text
B0: local 1,   frontier 2,    depth 0
B1: local 3,   frontier 21,   depth 1
B2: local 892, frontier 2450, depth 25
```

The frontier is recorded, not recursively opened. The full unbounded cone, selected Mathlib expansion, trust cost, and minimal sufficient boundary remain unknown. No boundary is called optimal or minimal.

This measures the tradeoff between reopening more project history and exposing a different external trust frontier. It does not combine declaration counts with transfer, storage, or wall-clock units.
